from django.urls import path
from .views import get_weather, index

urlpatterns = [
    path('api/weather/<str:city>/', get_weather, name='get_weather'),
]