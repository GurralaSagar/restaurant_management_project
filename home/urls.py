from django.urls import path

from .views import *

urlpatterns = [
    path("",home_view,name='home'),
    path('restaurant/',home_view,name='restaurant'),
    path('contact/',contact_view,name='contact'),
    path('about/',about_view, name='about'),
    path('menu/', MenuListView.as_view(), name='menu-list'),
    path("reservations/", reservations_view, name="reservations"),
    #path("feedback/",views.feedback_view, name="feedback"),
]