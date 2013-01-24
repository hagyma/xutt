from django.contrib import admin

from models import Project, Publication, Book

class ProjectAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'created_at', 'updated_at' )

    class Media:
        js = ('/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',)

class PublicationAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'created_at', 'updated_at' )

    class Media:
        js = ('/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',)

class BookAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'created_at', 'updated_at' )

    class Media:
        js = ('/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',)

admin.site.register(Project, ProjectAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Book, BookAdmin)