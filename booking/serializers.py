from rest_framework import serializers
from .models import Class, Booking

# Serializer for Class model
class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'

# Serializer for Booking model - for book a spot
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

# Serializer for get booking details
class BookingSummarySerializer(serializers.ModelSerializer):
    class_name = serializers.CharField(source = 'class_id.name')
    joining_date = serializers.DateTimeField(source = 'class_id.datetime')
    instructor = serializers.CharField(source = 'class_id.instructor')

    class Meta:
        model = Booking
        fields = ['class_name','joining_date','instructor']