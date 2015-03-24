from django.shortcuts import render

#import views
from django.views.generic import ListView
from datatableview.views import DatatableView

from speaker.models import SpeakerInfo


# Create your views here.
class SpeakerView(DatatableView):
    model = SpeakerInfo
    datatable_options = {
            'columns': [
                'last_name', 'first_name', 'email', 'mobile_phone', 'address_1', 'address_2', 'city', 'state', 'postal_code', 'country'
                ]
            }

speaker_list = SpeakerView.as_view()
