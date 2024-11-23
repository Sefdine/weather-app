import requests
from django.http import JsonResponse
from django.shortcuts import render
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Create your views here.

def get_weather(request, city):
    API_KEY = os.getenv('API_KEY')
    url = f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no'
    response = requests.get(url)
    if response.status_code == 200:
        return JsonResponse(response.json())
    else:
        return JsonResponse({'error': 'City not found'}, status=404)