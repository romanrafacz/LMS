from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required

from speaker.views import SpeakerView

urlpatterns = patterns('speaker.views',
        url(r'^$', login_required(SpeakerView.as_view())),
        )
