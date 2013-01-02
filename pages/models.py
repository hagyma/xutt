from django.db import models

from menu.models import Menu

from transmeta import TransMeta

class Page(models.Model):
    __metaclass__ = TransMeta

    menu = models.ForeignKey(Menu)
    title = models.CharField(max_length=30, blank=True, verbose_name=u'Title')
    description = models.TextField(verbose_name=u'Content')

    class Meta:
        translate = ('title', 'description', )

    def __unicode__(self):
        return self.title
