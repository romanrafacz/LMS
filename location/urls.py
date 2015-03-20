from django.conf.urls import patterns, url, include


urlpatterns = patterns('location.views',
    url(r'^$',
        view='location_list', name='location_list'
    ),
)
