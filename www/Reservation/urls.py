# -*- coding:Utf-8 -*-

from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
	url(r'^$', views.reserve, name="Reserve"),
)
