from django.db import models
from django.urls import reverse
# Create your models here.
   
class Building(models.Model):
    Street = models.CharField(max_length=50)
    Number = models.IntegerField()
    
   
    def __str__(self):
        return self.Street
    
    def get_absolute_url(self):
            return reverse("management:building_list")

class Apartment(models.Model):
    Number = models.IntegerField()
    Monthly_rent = models.IntegerField()
    Building = models.ForeignKey(Building, on_delete=models.CASCADE, null=False)
    

    def __str__(self):
        return  "%s apt %s" % (self.Building, self.Number)


    def get_absolute_url(self):
        return reverse('management:apartment_list')

class Tenant(models.Model):
    Apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, null=False)
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    GENDER_TYPES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    Gender = models.CharField(max_length=1, choices=GENDER_TYPES)
    Age = models.IntegerField()
    
    def __str__(self):
            return f"{self.First_name} {self.Last_name}"
    
    def get_absolute_url(self):
            return reverse('management:tenant_list')
    
    class meta:
        ordering = ["First_name"]