# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _

from datetime import date, timedelta, datetime

from www.Reservation.models import Reservation


class ReservationForm(forms.ModelForm):
	date = forms.DateField(input_formats =(
								'%Y-%m-%d',
							 	'%m/%d/%Y',
							 	'%m/%d/%y',
							 	'%d/%m/%Y',
							 	'%d/%m/%y',
						 	), error_messages={'invalid': _(u'Please enter valid date with format in : 1990-05-28, 05/28/1987, 03/27/06, 30/05/1996, 30/08/06')} )

	class Meta:
		model = Reservation
		exclude = ('table_numbers',)

	def clean(self):
		cleaned_data = super(ReservationForm, self).clean()
		selected_date = cleaned_data.get('date')
		selected_time = cleaned_data.get('time')
		if selected_date < date.today():
			raise forms.ValidationError(_(u"La date ne peut être inférieur à la date du jour"))
		elif selected_date == date.today():
			now = datetime.now()
			today = datetime.today()
			reserve_time = today.replace(hour=selected_time.hour, minute=selected_time.minute, second=selected_time.second, microsecond=selected_time.microsecond)
			if reserve_time < now :
				raise forms.ValidationError(_(u"L'heure de réservation est déjà passée"))
			if reserve_time >= now and now >= reserve_time - timedelta(seconds=900):
				raise forms.ValidationError(_(u"Vous devez réserver plus de 15 minutes à l'avance"))
		return cleaned_data
