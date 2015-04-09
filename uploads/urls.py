from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required

from uploads import views

urlpatterns = patterns('',
    url(r'^$',
        login_required(views.PartListView.as_view())
    ),
    url(r'^upload$', views.upload_file, name='upload_file')
#    url(r'^upload_data/$', view='UploadFile' name='UploadFile'),
)
