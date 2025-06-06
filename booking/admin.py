from django.contrib import admin
from .models import Class, Booking

# Class model admin.
@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Class._meta.fields]


@admin.register(Booking)
class ClassAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Booking._meta.fields]
