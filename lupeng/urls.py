from django.conf.urls import patterns, include, url
from filebrowser.sites import site
from django.conf import settings

from pages.views import index
from menu.views import show_menu_content

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lupeng.views.home', name='home'),
    # url(r'^lupeng/', include('lupeng.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^i18n/', include('django.conf.urls.i18n')),

    url(r'^$', index, name='index'),

    url(r'^(?P<slug>\w+)/', show_menu_content, name='show_content'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^%s/(?P<path>.*)$' % settings.STATIC_URL.strip('/'), "django.views.static.serve", {"document_root": settings.STATIC_ROOT}),
    )
    urlpatterns += patterns('',
        url(r'^%s/(?P<path>.*)$' % settings.MEDIA_URL.strip('/'), "django.views.static.serve", {"document_root": settings.MEDIA_ROOT}),
    )
