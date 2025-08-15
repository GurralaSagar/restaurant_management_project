from django.urls import path
from .views import *
from .views import MenuListView

urlpatterns = [
    path("",views.home_view,name='home'),
    path('restaurant/',views.home_view,name='restaurant'),
    path('contact/',views.contact_view,name='contact'),
    path('about/',views.about_view, name='about'),
    path('menu/', MenuListView.as_view(), name='menu-list'),
]