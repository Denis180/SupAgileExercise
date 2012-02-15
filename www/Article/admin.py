from django.contrib import admin

from models import Article
import settings

class ArticleAdmin(admin.ModelAdmin):
	list_display	= ("title", "date")
	ordering		= ("title", "date")
	search_fields	= ("title", "date")
	class Media:
		js = [
			settings.ADMIN_MEDIA_PREFIX+'tinymce/jscripts/tiny_mce/tiny_mce.js',
			settings.MEDIA_URL+'js/tinymce_setup/tinymce_setup.js',
		]

admin.site.register(Article, ArticleAdmin)