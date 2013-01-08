from django.db import models

from transmeta import TransMeta

from autoslug import AutoSlugField

MAX_ORDER = 10

ORDER_CHOICES = [(i,i) for i in xrange(0, MAX_ORDER+1)]

ORDER_CHOICES[0] = (0, 'Main')

class Menu(models.Model):
    __metaclass__ = TransMeta

    order = models.IntegerField(choices=ORDER_CHOICES, unique=True)
    title = models.CharField(max_length=30, blank=True, verbose_name=u'Title')
    slug = AutoSlugField(populate_from='title')

    class Meta:
        translate = ('title', 'slug', )

    def __unicode__(self):
        return '%s, (%s)' %  (self.title_en, self.title_zh_cn)
