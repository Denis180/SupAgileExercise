# -*- coding:Utf-8 -*-

from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib import messages

from models import *

from Reservation.models import PERSON_ON_TABLE, TABLE_NUMBER, Reservation
from Reservation.forms import ReservationForm


import math

def Home(request):
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
				return render_to_response('Front/Home.html', {"reservation_form" : form},context_instance=RequestContext(request))
			else:
				form.table_numbers = table_need
				reservation = form.save(commit=False)
				reservation.table_numbers = table_need
				reservation.save()
				messages.success(request, u"Réservation effectuée avec succès")
				return HttpResponseRedirect(reverse('Home'))
		else:
			return render_to_response('Front/Home.html', {"reservation_form" : form},context_instance=RequestContext(request))
	else:
		form = ReservationForm()
	return render_to_response('Front/Home.html', {"reservation_form" : form},context_instance=RequestContext(request))

def List(request):
	entrees		= Item.objects.filter(category = "START")
	viandes		= Item.objects.filter(category = "MEAT")
	desserts	= Item.objects.filter(category = "DESSERT")

	return render_to_response('Front/List.html',{
		"entrees"	: entrees,
		"viandes"	: viandes,
		"desserts"	: desserts
	}, context_instance=RequestContext(request))
