from django.shortcuts import render
from rest_framework import generics
from rest_framework.filters import SearchFilter
# Create your views here.

from .models import City, Day, Weather
from .serializers import CitySerializer, DaySerializer, WeatherSerializer, WeatherCitySerializer


class DayApiView(generics.ListAPIView):
    serializer_class = DaySerializer
    queryset = Day.objects.all()


class CityApiView(generics.ListAPIView):
    serializer_class = CitySerializer
    queryset = City.objects.all()


class WeatherCityApiView(generics.ListAPIView):
    serializer_class = WeatherCitySerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name',)
    queryset = City.objects.prefetch_related("weather")


class WeatherRetrieve(generics.RetrieveAPIView):
    serializer_class = WeatherSerializer
    queryset = Weather.objects.select_related("city")
