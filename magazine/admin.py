from django.contrib import admin


from .models import *


class MagazineAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'photo_magazine', 'time_create', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)





class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)




admin.site.register(Magazine, MagazineAdmin)
admin.site.register(Category, CategoryAdmin)

