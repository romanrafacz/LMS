from django.shortcuts import render

from registration.forms import UserForm

# Create your views here.

def signup(request):
    userform = UserForm()
    return render(request, 'registration/sign_up.html', {'userform':userform})
