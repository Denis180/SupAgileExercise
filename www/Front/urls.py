# -*- coding:Utf-8 -*-

from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
	url(r'^$', views.Home, name="Home"),
	url(r'^Carte/$', views.List, name="List"),
	url(r'^Contact/$', views.Contact, name="Contact"),
)
