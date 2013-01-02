from django.db import models

from transmeta import TransMeta

from autoslug import AutoSlugField

ORDER_CHOICES = (
    (1, 'First'),
    (2, 'Second'),
    (3, 'Third'),
    (4, 'Fourth'),
    (5, 'Fifth'),
    (6, 'Sixth'),
    (7, 'Seventh'),
    (8, 'Eighth'),
    (9, 'Ninth'),
    (10, 'Tenth'),
    )

class Menu(models.Model):
    __metaclass__ = TransMeta

    order = models.IntegerField(choices=ORDER_CHOICES, )
    title = models.CharField(max_length=30, blank=True, verbose_name=u'Title')
    slug = AutoSlugField(populate_from='title')

    class Meta:
        translate = ('title', 'slug', )

    def __unicode__(self):
        return self.title
