# -*- coding:Utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from filebrowser.sites import site

from django.contrib import admin
import settings

admin.autodiscover()

urlpatterns = patterns('',

    # Examples:
    # url(r'^$', 'www.views.home', name='home'),
    # url(r'^www/', include('www.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    url(r'^admin/filebrowser/', include(site.urls)),
     url(r'^site-media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    (r'^grappelli/', include('grappelli.urls')),
    (r'^localeurl/', include('localeurl.urls')),
    (r'', include('Front.urls')),
    (r'', include('Article.urls')),
)
