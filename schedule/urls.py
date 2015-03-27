from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required

from schedule.views import ScheduleListView

from schedule.views import JMClassView

urlpatterns = patterns('schedule.views',
    url(r'^$', login_required(ScheduleListView.as_view())),
    url(r'^/jm_detail', login_required(JMClassView.as_view())),
)
