from django.urls import path
from . import views

app_name = "preference"

urlpatterns = [
    path('get_states/', views.get_states, name='get_states'),
    path('get_cities/', views.get_cities, name='get_cities'),
    path('get_locations/', views.get_locations, name='get_locations'),
    path('', views.preferencee, name='preferencee'),
]