from django.shortcuts import render

from django.contrib.auth.models import User

# Create your views here.

def signup(request):
    userform = User()
    return render(request, 'registration/sign_up.html', {'userform':userform})
