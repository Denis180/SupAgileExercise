# -*- coding:Utf-8 -*-

from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib import messages

from models import *

from Reservation.models import PERSON_ON_TABLE, TABLE_NUMBER, Reservation
from Reservation.forms import ReservationForm
from Article.models import Article

import math

def Home(request):

	from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

	article_list = Article.objects.all().order_by('date')
	print article_list
	paginator = Paginator(article_list, 5)
	page = request.GET.get('page')
	try:
		articles = paginator.page(page)
	except (PageNotAnInteger, TypeError):
		articles = paginator.page(1)
	except EmptyPage:
		articles = paginator.page(paginator.num_pages)

	if request.method == "POST":
		form = ReservationForm(request.POST)
		table_disp = TABLE_NUMBER
		if form.is_valid():
			data = form.cleaned_data
			for reservation in Reservation.objects.filter(date = data['date'], time = data['time']):
				table_disp -= reservation.table_numbers

			temp = float(request.POST['numbers'])/float(PERSON_ON_TABLE)
			table_need = int(math.ceil(temp))

			if table_disp < table_need:
				messages.error(request, u"Il n'y a plus assez de tables disponibles pour votre réservation")
				return render_to_response('Front/Home.html', {"reservation_form" : form, "articles": articles},context_instance=RequestContext(request))
			else:
				form.table_numbers = table_need
				reservation = form.save(commit=False)
				reservation.table_numbers = table_need
				reservation.save()
				messages.success(request, u"Réservation effectuée avec succès")
				return HttpResponseRedirect(reverse('Home'))
		else:
			return render_to_response('Front/Home.html', {"reservation_form" : form, "articles": articles},context_instance=RequestContext(request))
	else:
		form = ReservationForm()
	return render_to_response('Front/Home.html', {"reservation_form" : form, "articles": articles},context_instance=RequestContext(request))

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
