from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required

from location.views import LocationListView

urlpatterns = patterns('location.views',
    url(r'^$',
        login_required(LocationListView.as_view())
    ),
)
