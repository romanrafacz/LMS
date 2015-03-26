from django.shortcuts import render

from django.views.generic import ListView
from uploads.models import Part

from datatableview.views import DatatableView

import csv

# Create your views here.

class PartListView(DatatableView):
    model = Part
    datatable_options = {
    'columns': [
        'training_id', 'name', 'company', 'phone'
    ]}

part_list = PartListView.as_view()

def UploadFile(request):
    if request.method == 'POST':
        with open(request.POST['file'], 'rU') as infile:
            reader = csv.reader(infile, delmiter=',', dialect='exce')
            for x in reader:
                enrollment = Part(training_id=x[0], name=x[1], company=[2], email=x[3], phone=[4])
                enrollment.save()
        return render(request, 'uploads/part_list.html', {})
    return render(request, 'uploads/part_list.html', {})
    

