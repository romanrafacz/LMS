from django.shortcuts import render

from django.views.generic import TemplateView

# Create your views here.

class ReportView(TemplateView):

    template_name = 'reporting/report_view.html'

    def get_context_data(self, **kwargs):
        jm_2013 = 256000
        jm_2014 = 315000
        jm_2015 = 141200
        return {'jm_2013':jm_2013, 'jm_2014': jm_2014, 'jm_2015': jm_2015}

reporting_view = ReportView.as_view()
