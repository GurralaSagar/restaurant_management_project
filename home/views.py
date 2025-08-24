from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.db import DatabaseError
from .models import MenuItem 
from datetime import datetime
from rest_framework.decorators import api_view
import requests

# Create your views here.

def home_view(request):
    return render(request,'home/index.html', {"current_year": datetime.now().year})

def homepage(request):
    phone_number = settings.RESTAURANT_PHONE_NUMBER
    return render(request,'homepage.html',{'phone_number':phone_number})

def home(request):
    # Fetch data from the API endpoint
    response = requests.get('http://127.0.0.1:8000/api/menu/')
    menu = response.json() if response.status_code == 200 else []
    return render(request, 'home.html',{'menu':menu})

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

def reservations_view(request):
    return render(request, "reservations.html")


@api_view(['GET'])
def menu_view(request):
    menu = [
        {
            "name" : "Margherita Pizza",
            "description" : "Classic cheese pizza with tomato sauce and moozzarrella.",
            "price" : 8.99
        },
        {
            "name" : "Veggie Burger",
            "description" : "Grilled vegetable patty served with lettuce, tomato, and sauce.",
            "price" : 6.49
        },
        {
            "name" : "Pasta Alfredo0",
            "description" : "Creamy Alfredo pasta with garlic and parmesan cheese.",
            "price" : 7.99
        }
    ]
    return Response(menu)