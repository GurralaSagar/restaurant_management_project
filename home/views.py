from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request):
    return render(request,'home/index.html')

def homepage(request):
    phone_number = settings.RESTAURANT_PHONE_NUMBER
    return render(request,'homepage.html',{'phone_number':phone_number})