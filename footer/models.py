from django.db import models
from transmeta import TransMeta

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
    logo = models.ImageField(upload_to='uploads/footer_images/', verbose_name=u'Logo', null=False)

    class Meta:
        verbose_name = u'Footer Logo'