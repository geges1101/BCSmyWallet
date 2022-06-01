import requests
from django.shortcuts import render

# Create your views here.

def index(request):
    url = 'https://bcschain.info/api/'

    res = requests.get(url) 
    print(res.text)

    return render(request, 'wallet/index.html')