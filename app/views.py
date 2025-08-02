from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

# Create your views here.
def index(request):
    city=request.GET.get('city','Bangalore')
    api_key='159213e6bbf6d9ed6eb410908065035b'

    api_url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    print(api_url)

    api=requests.get(api_url).json()
    temprature=api['main']['temp']
    country=api['sys']['country']
    city=api['name']

    return render(request,'index.html',{'temperature':temprature,'country':country,'city':city})
