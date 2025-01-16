from django.urls import path               #jab hum apne app1 folder me urls.py file bante hai tab ye code karte hai 
from app1 import views
urlpatterns = [
    path('contact/', views.contact_form),   
]