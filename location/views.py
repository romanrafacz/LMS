from django.shortcuts import render

from django.views.generic import ListView

from location.models import  JMWLocationInfo
from datatableview.views import DatatableView

# Create your views here.

class LocationListView(DatatableView):
    model = JMWLocationInfo 
    datatable_options = {
             'columns': [
                'description', 'street', 'city', 'state', 'postal_code', 'phone'
                ]
            }

location_list = LocationListView.as_view()
