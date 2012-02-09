# -*- coding:Utf-8 -*-

from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import *

def Home(request):
	return render_to_response('Front/Home.html',{},context_instance=RequestContext(request))

def List(request):
	entrees		= Item.objects.filter(category = "START")
	viandes		= Item.objects.filter(category = "MEAT")
	desserts	= Item.objects.filter(category = "DESSERT")
	return render_to_response('Front/List.html',{
		"entrees"	: entrees,
		"viandes"	: viandes,
		"desserts"	: desserts
	},context_instance=RequestContext(request))