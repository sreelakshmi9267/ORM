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

# Register your models here.

