from django.shortcuts import render

from registration.forms import UserForm

from django.contrib.auth.models import User

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
        user = User.objects.create_superuser(username=request.POST['username'], email=request.POST['email'], password=request.POST['password'])
        user.save()
        return render(request, 'registration/registration_response.html', {'message':message})

    userform = UserForm(data=request)
    return render(request, 'registration/registration_response.html', {'userform':userform, 'message':message})


