from django.db import models


# Create your models here.

class Weather(models.Model):
    humidity = models.IntegerField()
    temprature = models.IntegerField()
    rosa = models.IntegerField()
    wind_speed = models.IntegerField()
    pressure = models.IntegerField()
    feels_like = models.IntegerField()
    uv_index = models.IntegerField()
    pollution = models.IntegerField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank="True", default='default.jpg')
    day = models.ForeignKey("Day", on_delete=models.CASCADE, related_name='weather')
    city = models.ForeignKey("City", on_delete=models.CASCADE, related_name='weather')


class Day(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
