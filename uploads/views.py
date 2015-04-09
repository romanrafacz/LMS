from django.shortcuts import render

from django.views.generic import ListView
from uploads.models import Part

## import File form
from uploads.forms import UploadForm

from datatableview.views import DatatableView

import csv

# Create your views here.

class PartListView(DatatableView):
    model = Part
    datatable_options = {
    'columns': [
        'jmw_name', 'name', 'email', 'company', 'phone'
    ]}

    def get_context_data(self, **kwargs):
        form = UploadForm()
        return {'form':form}

part_list = PartListView.as_view()

def upload_file(request):
    if request.method == 'POST':
        with open(request.POST['file'], 'rU') as infile:
            reader = csv.reader(infile, delimiter=',', dialect='excel')
            for x in reader:
                enrollment = Part(jmw_name=x[0], name=x[1], company=x[2], email=x[3], phone=x[4])
                enrollment.save()
        return render(request, 'uploads/part_list.html', {})

    return render(request, 'uploads/part_list.html', {})
    

