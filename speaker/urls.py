from django.conf.urls import patterns, url, include

urlpatterns = patterns('speaker.views',
        url(r'^$', view='speaker_list', name='speaker_list'),
        )
