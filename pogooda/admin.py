from django.contrib import admin

# Register your models here.
from .models import Day, City, Weather

admin.site.register(Day)
admin.site.register(City)
admin.site.register(Weather)