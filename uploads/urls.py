from django.conf.urls import patterns, url, include


urlpatterns = patterns('uploads.views',
    url(r'^$',
        view='part_list', name='part_list'
    ),
#    url(r'^upload_data/$', view='UploadFile' name='UploadFile'),
)
