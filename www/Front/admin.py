# -*- coding:Utf-8 -*-

from django.contrib import admin
from models import Menu, Item

class MenuAdmin(admin.ModelAdmin):
	list_display	= ("name", "text", "price")
	ordering		= ("name", "text", "price")
	search_fields	= ("name", "text")

class ItemAdmin(admin.ModelAdmin):
	list_display	= ("category", "name", "price")
	list_filter		= ("category",)
	ordering		= ("category",)
	search_fields	= ("name",)
	
admin.site.register(Menu, MenuAdmin)
admin.site.register(Item, ItemAdmin)