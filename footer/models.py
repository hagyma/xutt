from django.db import models
from transmeta import TransMeta

MAX_ORDER = 10

ORDER_CHOICES = [(i,i) for i in xrange(1, MAX_ORDER+1)]

# Create your models here.
class Footer_Info(models.Model):
    __metaclass__ = TransMeta

    text = models.TextField(verbose_name=u'Footer Text')

    class Media:
        js = [
            '/static/admin/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/path/to/your/tinymce_setup.js',
        ]

    class Meta:
        verbose_name = u'Footer Info'
        translate = ('text', )

class Footer_Logos(models.Model):
    order = models.IntegerField(choices=ORDER_CHOICES, unique=True, verbose_name=u'Order')
    title = models.CharField(max_length=30, blank=True, verbose_name=u'Title')
    link = models.URLField(max_length=255, verbose_name=u'Link')
    logo = models.ImageField(upload_to='uploads/footer_images/', verbose_name=u'Logo', null=False)

    class Meta:
        verbose_name = u'Footer Logo'