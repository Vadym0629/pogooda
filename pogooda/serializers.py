from rest_framework import serializers
from .models import City, Day, Weather


class HalfDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = ['name']


class HalfWeatherSerializer(serializers.ModelSerializer):
    day = HalfDaySerializer()

    class Meta:
        model = Weather
        fields = [
            'id',
            "humidity",
            "temprature",
            "wind_speed",
            'photo',
            'day',
        ]


class WeatherCitySerializer(serializers.ModelSerializer):
    weather = HalfWeatherSerializer(many=True)

    class Meta:
        model = City
        fields = ['id', 'name', "weather"]


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name']


class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = ['id', 'name']


class WeatherSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    day = DaySerializer()
    class Meta:
        model = Weather
        fields = [
            'id',
            "humidity",
            "temprature",
            "rosa",
            "wind_speed",
            "pressure",
            "feels_like",
            "uv_index",
            "pollution",
            'photo',
            "city",
            'day',
        ]

