from django.shortcuts import render
import requests

# Create your views here.

from django.http import HttpResponse


def index(request):
    #return HttpResponse("Hello, world. You're at the testing index.")
    return render(request,'index.html')

def home(request):
    url = "https://api-mainnet.magiceden.dev/v2/collections/y00ts/activities?offset=0&limit=100"

    #url = 'https://api.covid19api.com/countries'
    #response = requests.get(url)


    response = requests.get(url).json()

    return render(request,'home.html',{'response':response})