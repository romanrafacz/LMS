from django.conf.urls import patterns, url, include


urlpatterns = patterns('photos.views',
    url(r'^$',
        view='photo_list', name='photo_list'
    ),
)
