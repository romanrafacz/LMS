from django.conf.urls import patterns, url, include

urlpatterns = patterns('schedule.views',
    url(r'^$', view='schedule_list', name='schedule_list'),
)
