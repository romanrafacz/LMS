from django.forms import ModelForm 

from location.models import JMWLocationInfo

class LocationForm(ModelForm):
    model = JMWLocationInfo 
    fields = '__all__'
