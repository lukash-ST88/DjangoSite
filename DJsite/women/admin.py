from django.contrib import admin
from .models import *

# Register your models here.


class WomenAdmin(admin.ModelAdmin): # Settings for admin panel
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published') # list of fields displayed in the admin panel
    list_display_links = ('id', 'title') # fields that are allowed to be edited by link
    search_fields = ('title', 'content') # fields that are allowed to search
    list_filter = ('is_published', 'time_create') # fields that could be filtered, sidebar in admin is created
    list_editable = ('is_published',) # list of fields that can be edited
    prepopulated_fields = {"slug": ("title",)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',) # "," - necessary for tuple
    prepopulated_fields = {"slug": ("name",)} # auto filling the slug field based on name field

admin.site.register(Women, WomenAdmin)
admin.site.register(Category,CategoryAdmin)
