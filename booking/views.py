from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from .models import Class, Booking
from .serializers import ClassSerializer, BookingSerializer, BookingSummarySerializer
import logging


logger = logging.getLogger('booking')

@api_view(['GET'])
def get_upcoming_classes(request):
    classes = Class.objects.filter(datetime__gte=timezone.now()).order_by('datetime')

    # Check if upcoming classes available 
    if classes.exists():
        serializer = ClassSerializer(classes, many=True)
        return Response(serializer.data)
    else:
        return Response({'type':'error','message':'Class does not exist.'},status=status.HTTP_200_OK)
    
@api_view(['POST'])
def book_class(request):
    serializer = BookingSerializer(data=request.data)
    if serializer.is_valid():

        # Check if class exist or not
        class_id = request.data.get('class_id')
        try:
            fitnes_class = Class.objects.get(id=class_id)
        except Class.DoesNotExist:
            logger.error('class name not found')
            return Response({'type':'error','message':'Class not exist.'}, status=status.HTTP_404_NOT_FOUND)
        
        # Check already booked by given email or not
        email = request.data.get('email')
        email_exist = Booking.objects.filter(class_id=fitnes_class, email=email).exists()
        if email_exist:
            logger.error(f'{email} is trying to book class twicw')
            return Response({'type':'error','message':'You have already booked this class.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Check spot available or not
        if fitnes_class.slots <=0:
            logger.error(f'{email} is trying to book but spot not available')
            return Response({'type':'error','message':'Sorry....Spot not Available.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # save booking and reduce spot
        serializer.save()
        fitnes_class.slots -=1
        fitnes_class.save()
        return Response({'type':'success','message':'Spot booked successfull.'}, status=status.HTTP_201_CREATED)
    else:
        logger.error(serializer.errors)
        return Response({'type':'error','message':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def get_booking_details(request):
    email = request.data.get('email')

    # Check email is given or not in request data
    if not email:
        logger.error('email required')
        return Response({'type':'erroe','message':'Email Required.'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Get All bookings made by the given email
    bookings = Booking.objects.filter(email=email).select_related('class_id') 

    # Check any booking made or not given by email
    if bookings.exists():
        serializer = BookingSummarySerializer(bookings, many=True)
        return Response(serializer.data)
    else:
        logger.error(f'{email} is trying to get bookings but there is no booking in the past.')
        return Response({'type':'error','message':'Booking not found.'}, status=status.HTTP_400_BAD_REQUEST)

