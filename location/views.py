from django.shortcuts import render

from django.views.generic import ListView

from location.models import  JMWLocationInfo 

# Create your views here.

class LocationListView(ListView):
    model = JMWLocationInfo 

location_list = LocationListView.as_view()
