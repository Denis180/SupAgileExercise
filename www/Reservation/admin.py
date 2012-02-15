from django.contrib import admin

from models import Reservation

class ReservationAdmin(admin.ModelAdmin):
	list_display	= ("__unicode__",)
	ordering		= ("date",)
	search_fields	= ("date",)
	list_filter = ('date',)

admin.site.register(Reservation, ReservationAdmin)
