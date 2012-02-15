# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _
from django.shortcuts import render_to_response, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib import messages

from www.Reservation.forms import ReservationForm
from www.Reservation.models import Reservation, TABLE_NUMBER, PERSON_ON_TABLE

import math

def reserve(request):
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
				mail_template = loader.get_template("Front/Mail/Reservation.txt")
				c = Context({
					"client_name"	: reservation.client_name,
					"numbers"		: reservation.numbers
				})
				send_mail(u"Un client vous a laissé un message", mail_template.render(c) , form.cleaned_data['sender_email'], [settings.EMAIL_HOST_USER], fail_silently=True)
				messages.success(request, u"Réservation effectuée avec succès")
				return HttpResponseRedirect(reverse('Home'))
		else:
			messages.error(request, u"Formulaire invalide")
			return render_to_response('Front/Home.html', {"reservation_form" : form},context_instance=RequestContext(request))
