# Ex02 Django ORM Web Application
# Date:20.09.2025
# AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).


## DESIGN STEPS
## STEP 1:
Clone the problem from GitHub

## STEP 2:
Create a new app in Django project

## STEP 3:
Enter the code for admin.py and models.py

## STEP 4:
Execute Django admin and create details for 10 books

# PROGRAM
```
models.py
from django.db import models
from django.contrib import admin
class Car(models.Model):
    car_name = models.CharField()
    car_model = models.CharField()
    release_date = models.DateField()
    car_color= models.CharField()
    car_price= models.IntegerField()
class CarAdmin(admin.ModelAdmin):
    list_display = ('car_name', 'car_model', 'release_date', 'car_color', 'car_price')

admin.py
from django.contrib import admin
from.models import Car,CarAdmin
admin.site.register(Car,CarAdmin)
```
# OUTPUT
![alt text](<Screenshot 2025-09-19 231800.png>)

# RESULT
Thus the program for creating a database using ORM hass been executed successfully
