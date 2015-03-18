from django.shortcuts import render

from django.views.generic import ListView
from photos.models import Photo


class PhotoListView(ListView):
    model = Photo

photo_list = PhotoListView.as_view()
