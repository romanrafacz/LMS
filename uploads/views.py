from django.shortcuts import render

from django.views.generic import ListView
from uploads.models import Part

from datatableview.views import DatatableView

# Create your views here.

class PartListView(DatatableView):
    model = Part
    datatable_options = {
    'columns': [
        'training_id', 'name', 'company', 'phone'
    ]}

part_list = PartListView.as_view()
