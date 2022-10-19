from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
# Register your models here.


class WomenAdmin(admin.ModelAdmin): # Settings for admin panel
    list_display = ('id', 'title', 'time_create', 'get_html_photo', 'is_published') # list of fields displayed in the admin panel
    list_display_links = ('id', 'title') # fields that are allowed to be edited by link
    search_fields = ('title', 'content') # fields that are allowed to search
    list_filter = ('is_published', 'time_create') # fields that could be filtered, sidebar in admin is created
    list_editable = ('is_published',) # list of fields that can be edited
    prepopulated_fields = {"slug": ("title",)}
    fields = ('title', 'slug', 'cat', 'content', 'photo', 'get_html_photo', 'is_published', 'time_create', 'time_update') # field in edition fields
    readonly_fields = ('time_create', 'time_update', 'get_html_photo') # non-editable fields
    save_on_top = True

    def get_html_photo(self, object): # for displaying mini photo in admin, object references to the current instance of women model
        if object.photo: # if not to add "if" django can put a error because of absence of a photo at one of instances
            return mark_safe(f"<img src='{object.photo.url}' width=50>") # mark_sefe does not screen code

    get_html_photo.short_description = 'Миниатюра' #overriding the name

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',) # "," - necessary for tuple
    prepopulated_fields = {"slug": ("name",)} # auto filling the slug field based on name field

admin.site.register(Women, WomenAdmin)
admin.site.register(Category,CategoryAdmin)

admin.site.site_title = 'Админ-панель сейта о женщинах' # attributes of site admin panel
admin.site.site_header = 'Админ-панель сайта о женщинах2'