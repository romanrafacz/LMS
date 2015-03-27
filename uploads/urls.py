from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required

from uploads.views import PartListView

urlpatterns = patterns('uploads.views',
    url(r'^$',
        login_required(PartListView.as_view())
    ),
#    url(r'^upload_data/$', view='UploadFile' name='UploadFile'),
)
