from django.conf.urls import url, patterns, include

from django.contrib.auth.decorators import login_required

from reporting.views import ReportView, RosterView

urlpatterns = patterns('reporting.views',
    url(r'^$', login_required(ReportView.as_view())),
    url(r'^roster$', login_required(RosterView.as_view()))

)