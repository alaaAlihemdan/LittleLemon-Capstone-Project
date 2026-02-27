# from django.db import models
# Create your models here.

from django.db import models

class Booking(models.Model):
    first_name = models.CharField(max_length=255)
    reservation_date = models.DateField()
    reservation_slot = models.SmallIntegerField(default=10)

    def __str__(self): 
        return self.first_name

class Menu(models.Model):
   name = models.CharField(max_length=255) # تأكد أنها name
   price = models.DecimalField(max_digits=10, decimal_places=2) 
   inventory = models.SmallIntegerField() 

   def __str__(self):
       return f'{self.name} : {str(self.price)}'