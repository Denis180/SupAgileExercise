from django.contrib import admin

from models import Reservation

class ReservationAdmin(admin.ModelAdmin):
	list_display	= ("__unicode__","client_name","phone","numbers","table_numbers","date",)
	ordering		= ("date",)
	search_fields	= ("date","client_name")
	list_filter = ('date',"numbers")

admin.site.register(Reservation, ReservationAdmin)
