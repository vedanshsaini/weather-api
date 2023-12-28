import requests
from django.shortcuts import render
import json


def get_weather(api_key, city):
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}'
    response = requests.get(url)

    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        try:
            data = response.json()
            return data
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return None
    else:
        print(f"Error: {response.status_code}")
        return None


def weather(request):
    api_key = 'a1573855edd44d66ba4114651232812'  # Replace with your actual WeatherAPI key
    city = 'London'
    weather_data = get_weather(api_key, city)

    if weather_data:
        context = {
            'city': city,
            'temperature': weather_data.get('current', {}).get('temp_c'),
            'condition': weather_data.get('current', {}).get('condition', {}).get('text'),
        }
    else:
        # Handle the case when weather_data is None
        context = {
            'city': city,
            'temperature': None,
            'condition': None,
        }

    return render(request, 'project_manager/templates/weather.html', context)
