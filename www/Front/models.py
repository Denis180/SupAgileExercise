# -*- coding:Utf-8 -*-

from django.db import models
from django.utils.translation import ugettext as _


class Menu(models.Model):
    """Menu"""
    
    name = models.CharField(max_length = 64, blank = True)
    price = models.DecimalField(max_digits = 5, decimal_places = 2)
    text = models.TextField(max_length = 2048)

class Course(models.Model):
    """Element à la carte"""
    CATEGORIES	= (
        ("STARTER", _("Starters")),
        ("MEAT", _("Meats")),
        ("DESSERT", _("Desserts"))
    )
    name = models.CharField(max_length = 128)
    category	= models.CharField(max_length = 64, choices = CATEGORIES)
    name		= models.CharField(max_length = 128)
    price		= models.DecimalField(max_digits = 5, decimal_places = 2)
