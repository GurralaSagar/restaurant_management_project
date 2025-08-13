from django.urls import path
from .views import *

urlpatterns = [
    path("",views.home_view,name='home'),
    path('restaurant/',views.home_view,name='restaurant'),
    path('contact/',views.contact_view,name='contact'),
    path('about/',views.about_view, name='about'),
]