from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required

from registration import views 

urlpatterns = patterns('',
    url(r'^$',
        views.signup, name='singup'
    ),
    url(r'^register$',
        views.register, name='register'
    ),
)
