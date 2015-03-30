from django.shortcuts import render

from registration.forms import UserForm

# Create your views here.

def signup(request):
    userform = UserForm()
    return render(request, 'registration/sign_up.html', {'userform':userform})

def register(request):
    userform = UserForm(data=request)
    if request.method == 'POST':
        if request.POST['access_code'] == 'turkey':
            message = 'success'
            return render(request, 'registration/registration_response.html', {'userform':userform, 'message':message})
        else:
            message = "access key is incorrect"
            return render(request, 'registration/sign_up.html', {'userform':userform, 'message':message})
    message = "access key is incorrect"
    return render(request, 'registration/sign_up.html', {'userform':userform, 'message':message})
