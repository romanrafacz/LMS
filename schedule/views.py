from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView
from datatableview.views import DatatableView

##import libraries for api pull
import requests
import json

from lms.models import JMWClassInfo, ClassPlSummary 

# Create your views here.
class ScheduleListView(DatatableView):
    template_name = 'schedule/schedule_list.html'
    model = JMWClassInfo
    datatable_options = {
        'columns': [
            "avnet_type_name", "jmw_name", "start_date", "end_date", "duration", "public", "class_status", "total_registered", "instructor_name", "tech", "labs"
        ]
    }

    def get_context_data(self, **kwargs):
        schedule_data = ""
        return {'schedule_data': schedule_data}


schedule_list = ScheduleListView.as_view()

class JMClassView(ListView):
    model = ClassPlSummary 
    template_name = 'schedule/class_summary.html'

