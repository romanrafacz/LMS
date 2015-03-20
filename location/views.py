from django.shortcuts import render

from django.views.generiv import ListView

from location.models import  

# Create your views here.

class LocationListView(ListView):
    model = JMWLocationInfo 

location_view = LocationListView.as_view()
