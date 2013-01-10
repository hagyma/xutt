from django.contrib import admin

from models import Footer_Info, Footer_Logos

class Footer_InfoAdmin(admin.ModelAdmin):
    list_display = ( ('text_en'), ('text_zh_cn'), )
    ordering = ()

class Footer_LogosAdmin(admin.ModelAdmin):
    list_display = ( ('logo_name'), )

    def logo_name(self, obj):
        try:
            if obj.logo:
                return u"%s" % ( obj.logo.__unicode__().split("/")[-1])
            else:
                return ""
        except IOError:
            return ""

    logo_name.allow_tags = True
    logo_name.short_description = u"Logo Name"

admin.site.register(Footer_Info, Footer_InfoAdmin )
admin.site.register(Footer_Logos, Footer_LogosAdmin)