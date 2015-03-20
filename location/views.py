from django.shortcuts import render

from django.views.generic import ListView

from location.models import  JMWLocationInfo
from datatableview.views import DatatableView

# Create your views here.

class LocationListView(DatatableView):
    model = JMWLocationInfo 

location_list = LocationListView.as_view()
