from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^(.+)$', 'cms.views.peticion'),
    url(r'^$', 'cms.views.lista'),
    url(r'^admin/', include(admin.site.urls)),
)
