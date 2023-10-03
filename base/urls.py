from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
]