# -*- coding:Utf-8 -*-

from django.contrib import admin
from models import Menu, Course
from django.contrib.auth.models import User, Group
from django.contrib.sites.models import Site

class MenuAdmin(admin.ModelAdmin):
	list_display	= ("name", "text", "price")
	ordering		= ("name", "text", "price")
	search_fields	= ("name", "text")

class CourseAdmin(admin.ModelAdmin):
	list_display	= ("category", "name", "price")
	list_filter		= ("category",)
	ordering		= ("category",)
	search_fields	= ("name",)
	
admin.site.register(Menu, MenuAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Site)