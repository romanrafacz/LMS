from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required

from schedule.views import JMClassView

urlpatterns = patterns('schedule.views',
    url(r'^$', view='schedule_list', name='schedule_list'),
    url(r'^/jm_detail', JMClassView.as_view()),
)
