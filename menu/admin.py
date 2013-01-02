from django.contrib import admin

from models import Menu

class MenuAdmin(admin.ModelAdmin):
    list_display = ( 'order', 'title' )
    ordering = ('order')

admin.site.register(Menu, MenuAdmin)
