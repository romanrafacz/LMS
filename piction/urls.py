from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'piction.views.index', name='index'),
    # url(r'^blog/', include('blog.urls')),
     url(r'^photos/', include('photos.urls')),
     url(r'^uploads/', include('uploads.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
