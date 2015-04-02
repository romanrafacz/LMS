from django.shortcuts import render

from django.views.generic import TemplateView

# Create your views here.

class ReportView(TemplateView):
    template_name = 'reporting/report_view.html'

reporting_view = ReportView.as_view()
