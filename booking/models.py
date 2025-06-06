from django.db import models
import uuid

# Classes model
class Class(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    instructor = models.CharField(max_length=100)
    slots = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
# Booking Model
class Booking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()