from django.contrib import admin

from models import Menu

class MenuAdmin(admin.ModelAdmin):
    list_display = ( 'order', 'title_en', 'title_zh_cn' )
    ordering = ('order', )

admin.site.register(Menu, MenuAdmin)
