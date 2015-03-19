from django.shortcuts import render

from django.views.generic import ListView
from uploads.models import Part

from datatableview.views import DatatableView

# Create your views here.

class PartListView(DatatableView):
    model = Part

part_list = PartListView.as_view()
