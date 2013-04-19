from django.conf.urls import patterns, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'megawatt.views.index'),
    url(r'^post/$', 'megawatt.views.index'),
    url(r'^update/(?P<field>.+)/(?P<id>\d+)/?$', 'megawatt.views.update'),
    url(r'^admin/', (admin.site.urls)),
)
