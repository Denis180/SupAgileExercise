# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _

from datetime import time

TABLE_NUMBER = 10
PERSON_ON_TABLE = 5

class Reservation(models.Model):
	
	TIME_CHOICES = (
		(time(12, 00, 00), '12H'),
		(time(13, 00, 00), '13H'),
		(time(19, 00, 00), '19H'),
		(time(20, 00, 00), '20H'),
		(time(21, 00, 00), '21H'),
	)

	email = models.EmailField(max_length=75, blank=False, null=False, verbose_name=_("E-mail"))
	client_name = models.CharField(max_length=32, blank=False, null=False, verbose_name=_("Name"))
	phone = models.IntegerField(max_length=16, blank=False, null=False, verbose_name=_("Phone"))
	numbers = models.IntegerField(max_length=2, blank=False, null=False, verbose_name=_("Seats"))
	table_numbers = models.IntegerField(max_length=2, blank=False, null=False, verbose_name=_("Tables"))
	date = models.DateField(blank=False, null=False, verbose_name=_("Date"))
	time = models.TimeField(choices=TIME_CHOICES, blank=False, null=False, default=TIME_CHOICES[0], verbose_name=_("Time"))

	class Meta:
		verbose_name = _(u'Reservation')
		verbose_name_plural = _(u'Reservations')

	def __unicode__(self):
		return _(u'Réservation du %(date)s à %(hour)s par %(name)s pour %(personnes)i personnes' % {'date' : self.date.strftime("%A %d. %B %Y"), 'hour' : self.time, 'name' : self.client_name, 'personnes' : self.numbers})