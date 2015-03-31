from django.shortcuts import render

from registration.forms import UserForm

# Create your views here.

def signup(request):
    return render(request, 'registration/sign_up.html', {})

def register(request):
    userform = UserForm()
    if request.method == 'POST':
        if request.POST['access_code'] == 'turkey':
            return render(request, 'registration/complete_signup.html', {'userform':userform})
        else:
            message = "access key is incorrect"
            return render(request, 'registration/sign_up.html', {'message':message})

    return render(request, 'registration/sign_up.html', {})

def complete_signup(request):
    userform = UserForm(data=request)

    if request.method == 'POST':
        message = 'success'
        return render(request, 'registration/registration_response.html', {'message':message})
        
    userform = UserForm(data=request)
    return render(request, 'registration/registration_response.html', {'userform':userform, 'message':message})


