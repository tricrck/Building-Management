from django.db import models

# Create your models here.

class Owner(models.model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)

class Pet(models.model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    animal_type = models.CharField(max_length=150)
    breed = models.CharField(max_length=150)
    pet_name = models.CharField(max_length=30)
    age = models.IntergerField(default=0)

class Appointment(models.model):
    