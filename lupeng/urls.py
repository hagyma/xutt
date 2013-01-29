from django.conf.urls import patterns, include, url
from filebrowser.sites import site
from django.conf import settings

from pages.views import index
from menu.views import show_menu_content

from archives.views import Projects, Publications, Books

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

    url(r'^projects/$', Projects.as_view(), name='projects'),
    url(r'^publications/$', Publications.as_view(), name='publications'),
    url(r'^books/$', Books.as_view(), name='books'),

)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^%s/(?P<path>.*)$' % settings.STATIC_URL.strip('/'), "django.views.static.serve", {"document_root": settings.STATIC_ROOT}),
    )
    urlpatterns += patterns('',
        url(r'^%s/(?P<path>.*)$' % settings.MEDIA_URL.strip('/'), "django.views.static.serve", {"document_root": settings.MEDIA_ROOT}),
    )

urlpatterns += patterns('',
    url(r'^(?P<slug>\w+)/', show_menu_content, name='show_content'),
    )
