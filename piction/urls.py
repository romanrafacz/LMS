from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'piction.views.index', name='index'),
    # url(r'^blog/', include('blog.urls')),
     url(r'^photos/', include('photos.urls')),
     url(r'^uploads/', include('uploads.urls')),
     url(r'^schedule/', include('schedule.urls')),
     url(r'^location/', include('location.urls')),
     url(r'^speaker/', include('speaker.urls')),
    url(r'^registration/', include('registration.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # authentication
    url(r'^accounts/login/', 'django.contrib.auth.views.login'),
    url(r'^login/', 'django.contrib.auth.views.login'),
    url(r'^logout/', 'django.contrib.auth.views.logout')
)
