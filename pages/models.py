from django.db import models

from menu.models import Menu

from transmeta import TransMeta

class Page(models.Model):
    __metaclass__ = TransMeta

    menu = models.ForeignKey(Menu)
    title = models.CharField(max_length=30, blank=True, verbose_name=u'Title')
    content = models.TextField(verbose_name=u'Content')

    class Media:
        js = [
            '/static/admin/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/path/to/your/tinymce_setup.js',
        ]

    class Meta:
        translate = ('title', 'content', )

    def __unicode__(self):
        return self.title
