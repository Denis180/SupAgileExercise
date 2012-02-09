# -*- coding:Utf-8 -*-

from django.db import models


class Menu(models.Model):
	"""Menu"""
	name		= models.CharField(max_length = 64)
	text		= models.TextField(max_length = 2048)
	price		= models.DecimalField(max_digits = 5, decimal_places = 2)
	class Media:
		js = [
			'/media/admin/tinymce/jscripts/tiny_mce/tiny_mce.js',
			'/path/to/your/tinymce_setup.js',
		]

class Item(models.Model):
	"""Element à la carte"""
	CATEGORIES	= (
		("START", "Entrées"),
		("MEAT", "Viandes"),
		("DESSERT", "Desserts")
	)

	category	= models.CharField(max_length = 64, choices = CATEGORIES)
	name		= models.CharField(max_length = 128)
	price		= models.DecimalField(max_digits = 5, decimal_places = 2)