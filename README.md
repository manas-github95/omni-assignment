# omni-assignment

1. Get All upcoming classes
   
Endpoint : GET / http://127.0.0.1:8000/classes

result:

 {
     "id": "0d0f1d68-8ddc-44b8-9423-7c01b6de72ef",
     "name": "Yoga",
     "datetime": "2025-06-12T12:29:58+05:30",
     "instructor": "Rekha",
     "slots": 20
 },
 {
     "id": "89cb6234-92bb-492d-9099-3b0adecd6f5f",
     "name": "Zumba",
     "datetime": "2025-06-16T12:30:31+05:30",
     "instructor": "Raj",
     "slots": 29
 },
 {
     "id": "50853d64-5bab-4d31-af64-4123fa8e90da",
     "name": "HIIT",
     "datetime": "2025-06-17T12:30:48+05:30",
     "instructor": "liman",
     "slots": 20
 }


2. Post a book
   
Endpoint : POST / http://127.0.0.1:8000/book

body :

{
    "class_id":"0d0f1d68-8ddc-44b8-9423-7c01b6de72ef",
    "name":"manas",
    "email":"manas@gmail.com"
}

result :

{
    "type": "success",
    "message": "Spot booked successfull."
}

If Again try to book then an error response will come like below.

{
    "type": "error",
    "message": "You have already booked this class."
}

3. Get booking details

Endpoint http://127.0.0.1:8000/bookings

body :
{
    "email":"manas@gmail.com"
}

Response :

 {
     "class_name": "Zumba",
     "joining_date": "2025-06-16T12:30:31+05:30",
     "instructor": "Raj"
 },
 {
     "class_name": "Yoga",
     "joining_date": "2025-06-12T12:29:58+05:30",
     "instructor": "Rekha"
 }



