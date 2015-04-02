from django.conf.urls import url, patterns, include

urlpatterns = patterns('reporting.views',
    url(r'^$', view='reporting_view', name='reporting_view')

)