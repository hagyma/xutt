from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404
from django.views.generic import View

from models import Project, Publication, Book

class BaseView(View):
    http_method_names = ['get', 'post',]

class Projects(BaseView):
	template = 'project.html'
	http_method_names = ['get', ]

	def get(self, request, *args, **kwargs):

		projects = Project.objects.all()

		project_pk = request.GET.get('project', None)
	
		project_item = None

		if project_pk:
			project_item = Project.objects.get(pk=project_pk)

		context = {
			'projects': projects,
			'project_item': project_item,

		}

		return TemplateResponse(request, self.template, context)

class Publications(BaseView):
	template = 'publication.html'
	http_method_names = ['get', ]

	def get(self, request, *args, **kwargs):

		publications = Publication.objects.all()

		publication_pk = request.GET.get('publication', None)

		publication_item = None

		if publication_pk:
			publication_item = Publication.objects.get(pk=publication_pk)

		context = {
			'publications': publications,
			'publication_item': publication_item,
		}

		return TemplateResponse(request, self.template, context)

class Books(BaseView):
	template = 'book.html'
	http_method_names = ['get', ]

	def get(self, request, *args, **kwargs):

		books = Book.objects.all()

		book_pk = request.GET.get('book', None)

		book_item = None

		if book_pk:
			book_item = Book.objects.get(pk=book_pk)

		context = {
			'books': books,
			'book_item': book_item,
		}

		return TemplateResponse(request, self.template, context)

"""
def archive(request):
	template_name = 'archive.html'

	projects = Project.objects.all()

	publications = Publication.objects.all()

	books = Book.objects.all()

	project_pk = request.GET.get('project', None)
	
	project_item = None

	if project_pk:
		project_item = Project.objects.get(pk=project_pk)

	publication_pk = request.GET.get('publication', None)

	publication_item = None

	if publication_pk:
		publication_item = Publication.objects.get(pk=publication_pk)

	book_pk = request.GET.get('book', None)

	book_item = None

	if book_pk:
		book_item = Book.objects.get(pk=book_pk)

	context = {
		'projects': projects,
		'project_item': project_item,
		'publication_item': publication_item,
		'book_item': book_item,
		'publications': publications,
		'books': books,
	}

	return TemplateResponse(request, template_name, context)
"""

