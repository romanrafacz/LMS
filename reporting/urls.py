from django.conf.urls import url, patterns, include

from django.contrib.auth.decorators import login_required

from reporting import views

urlpatterns = patterns('reporting.views',
    url(r'^$', login_required(views.ReportView.as_view())),
    url(r'^roster$', login_required(views.RosterView.as_view())),
    url(r'^class_roster/(?P<pk>\d+)/$', login_required(views.RosterByCourse.as_view())),


)