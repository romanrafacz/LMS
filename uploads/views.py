from django.shortcuts import render

from django.views.generic import ListView
from uploads.models import Part

# Create your views here.

class PartListView(ListView):
    model = Part

part_list = PartListView.as_view()
