from django.db import models

from menu.models import Menu

from transmeta import TransMeta

class Page(models.Model):
    __metaclass__ = TransMeta

    menu = models.OneToOneField(Menu)
    title = models.CharField(max_length=30, blank=True, null=True, verbose_name=u'Title')
    content = models.TextField(verbose_name=u'Content')
    image = models.ImageField(upload_to='uploads/', blank=True, null= True, verbose_name=u'Image')

    class Media:
        js = [
            '/static/admin/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/path/to/your/tinymce_setup.js',
        ]

    class Meta:
        translate = ('title', 'content', )

    def __unicode__(self):
        return self.title

"""
    limit_choices_to = {'used':False}
    def save(self, *args, **kwargs):

        menu = self.menu

        if menu:
            m = Menu.objects.get(title_en=menu.title)
            m.used = True
            m.save()

        return super(Page, self).save(*args, **kwargs)
"""
