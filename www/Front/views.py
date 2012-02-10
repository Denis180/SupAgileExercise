# -*- coding:Utf-8 -*-

from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import *

def Home(request):
	return render_to_response('Front/Home.html',{},context_instance=RequestContext(request))

def List(request):
	menus		= Menu.objects.all()
	starters	= Course.objects.filter(category = "STARTER")
	meats		= Course.objects.filter(category = "MEAT")
	desserts	= Course.objects.filter(category = "DESSERT")
	return render_to_response('Front/List.html',{
		"menus"		: menus,
		"starters"	: starters,
		"meats"		: meats,
		"desserts"	: desserts
	},context_instance=RequestContext(request))

def Contact(request):
	return render_to_response('Front/Contact.html',{},context_instance=RequestContext(request))