from django.urls import path
from .views import DayApiView, CityApiView, WeatherCityApiView, WeatherRetrieve

urlpatterns = [
    path('day/', DayApiView.as_view()),
    path('city/', CityApiView.as_view()),
    path('weather/', WeatherCityApiView.as_view()),
    path('weather/<int:pk>', WeatherRetrieve.as_view()),

]