from django.forms import ModelForm 

class LocationForm(ModelForm):
    model = JMWLocationInfo 
    fields = '__all__'
