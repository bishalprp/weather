from django.shortcuts import render
import requests
from django.contrib import messages

# Create your views here.

def index(request):
    if 'city' in request.POST:
        city=request.POST['city']

    else:
        city='kathmandu'

    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=1bda135d96dbbab13461f42332fed194"
    param={'units':'metric'}
    data=requests.get(url,param).json()    #it converts json to dictionary

    try:
        temp=data['main']['temp']
        desc=data['weather'][0]['description']
        wind=data['wind']['speed']
        humidity=data['main']['humidity']
        icon=data['weather'][0]['icon']
        return render(request,'index.html',{'temp':temp,"city":city,"wind":wind,"desc":desc,"humidity":humidity,"icon":icon})

    except:
        temp=0
        desc="there is no city"
        messages.error(request,"There is no such city!!")
        return render(request,'index.html',{'temp':temp,"city":city,"desc":desc,})