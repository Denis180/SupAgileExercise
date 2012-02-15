# -*- coding:Utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
import settings

class Article(models.Model):
	"""Article"""
	title		= models.CharField(max_length = 64, blank = False, null = False)
	text		= models.TextField(max_length = 2048)
	date		= models.DateTimeField(auto_now_add = True)
	
	class Meta:
		verbose_name = _('Article')
		verbose_name_plural = _('Articles')

	def __unicode__(self):
		return _(u'Article : %(title)s du  %(date)s' % {'title' : self.title, 'date' : self.date})