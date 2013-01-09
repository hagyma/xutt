from django.contrib import admin

from models import Footer_Info, Footer_Logos

class Footer_InfoAdmin(admin.ModelAdmin):
    list_display = ( ('text_en'), ('text_zh_cn'), )
    ordering = ()

class Footer_LogosAdmin(admin.ModelAdmin):
    list_display = ( ('logo'), )

admin.site.register(Footer_Info, Footer_InfoAdmin )
admin.site.register(Footer_Logos, Footer_LogosAdmin)