# -*- coding:Utf-8 -*-

from django.db import models
from django.utils.translation import ugettext as _
import settings


class Menu(models.Model):
	"""Menu"""
	name		= models.CharField(max_length = 64, blank = True)
	text		= models.TextField(max_length = 2048)
	price		= models.DecimalField(max_digits = 5, decimal_places = 2)
	

class Course(models.Model):
	"""Element à la carte"""
	CATEGORIES	= (
		("STARTER", _("Starters")),
		("MEAT", _("Meats")),
		("DESSERT", _("Desserts"))
	)

	category	= models.CharField(max_length = 64, choices = CATEGORIES)
	name		= models.CharField(max_length = 128)
	price		= models.DecimalField(max_digits = 5, decimal_places = 2)
