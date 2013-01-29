from django.db import models

from transmeta import TransMeta

class Project(models.Model):
	__metaclass__ = TransMeta

	title = models.CharField(max_length=64, verbose_name=u'Title')
	description = models.TextField(verbose_name=u'Description')
	image = models.ImageField(upload_to='uploads/project/', blank=True, null= True, verbose_name=u'Image')

	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True, editable=False)

	class Meta:
		translate = ('title', 'description', 'image')

	class Media:
		js = [
			'/static/admin/tinymce/jscripts/tiny_mce/tiny_mce.js',
			'/static/path/to/your/tinymce_setup.js',
		]

	def __unicode__(self):
		return u'%s' % self.title

class Book(models.Model):
	__metaclass__ = TransMeta

	title = models.CharField(max_length=64, verbose_name=u'Title')
	description = models.TextField(verbose_name=u'Description')
	image = models.ImageField(upload_to='uploads/book/', blank=True, null= True, verbose_name=u'Image')

	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True, editable=False)

	class Meta:
		translate = ('title', 'description', 'image')

	class Media:
		js = [
			'/static/admin/tinymce/jscripts/tiny_mce/tiny_mce.js',
			'/static/path/to/your/tinymce_setup.js',
		]

	def __unicode__(self):
		return u'%s' % self.title

class Publication(models.Model):
	__metaclass__ = TransMeta

	title = models.CharField(max_length=64, verbose_name=u'Title')
	description = models.TextField(verbose_name=u'Description')
	image = models.ImageField(upload_to='uploads/publication/', blank=True, null= True, verbose_name=u'Image')

	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True, editable=False)

	class Meta:
		translate = ('title', 'description', 'image' )

	class Media:
		js = [
			'/static/admin/tinymce/jscripts/tiny_mce/tiny_mce.js',
			'/static/path/to/your/tinymce_setup.js',
		]
		
	def __unicode__(self):
		return u'%s' % self.title
