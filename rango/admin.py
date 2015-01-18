from django.contrib import admin
from rango.models import Category, Page

# Register your models here.

#View for Catgeory
class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}

#View for the admin page
class PageAdmin(admin.ModelAdmin):
	list_display = ('title','category','url')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)

