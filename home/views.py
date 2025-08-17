from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.db import DatabaseError
from .models import MenuItem 
from datetime import datetime

# Create your views here.

def home_view(request):
    return render(request,'home/index.html', {"current_year": datetime.now().year})

def homepage(request):
    phone_number = settings.RESTAURANT_PHONE_NUMBER
    return render(request,'homepage.html',{'phone_number':phone_number})

def home(request):
    context = {
        'restaurant_name':'Delicious Bites'
    }
    return render(request, 'home.html',context)

def contact_view(request):
    return render(request,'contact.html')

def about_view(request):
    return render(request, 'about.html')


class MenuListView(APIView):
    def get(self, request):
        # Hardcoded list of menu items
        menu_items = [
            {"id": 1, "name": "Margherita Pizza", "price": 250, "category": "Pizza"},
            {"id": 2, "name": "veg Burger", "price": 150, "category": "Burgers"},
            {"id": 3, "name": "Pasta Alfredo", "price": 300, "category": "Pasta"},
            {"id": 4, "name": "Caesar salad", "price": 200, "category": "Salads"},
        ]
        return Response(menu_items, status=status.HTTP_200_OK)


def custom_404(request, exception):
    return render(request, "404.html", status=404)


def menu_items_view(request):
    try:
        items = MenuItem.objects.all().values("id", "name", "price")
        data = list(items)
        return JsonResponse({"status": "success", "menu_items": data}, status=200)
    
    except DatabaseError as e:
        # Handle database connection/query errors
        return JsonResponse({
            "status" : "error",
            "message" : "Database error occurred. Please try again later."
        }, status=500)

    except Exception as e:
        # Catch any other unexpected error
        return JsonResponse({
            "status" : "error",
            "message" : "Something went wrong. Please try again."
        }, status=500)