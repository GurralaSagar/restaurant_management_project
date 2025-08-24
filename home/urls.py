from django.urls import path
from .views import *

urlpatterns = [
    path("",views.home_view,name='home'),
    path('restaurant/',views.home_view,name='restaurant'),
    path('contact/',views.contact_view,name='contact'),
    path('about/',views.about_view, name='about'),
    path('menu/', MenuListView.as_view(), name='menu-list'),
    path("reservations/", views.reservations_view, name="reservations"),
    path("feedback/", views.feedback_view, name="feedback"),
    path('api/menu/',menu_view,name='menu'),
]