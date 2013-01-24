from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404

from models import Project, Publication, Book

def archive(request):
	template_name = 'archive.html'

	context = {}

	return TemplateResponse(request, template_name, context)

def project(request):
	template_name = 'archiveproject.html'

	projects = Project.objects.all()

	context = {
		'projects': projects,
	}

	return TemplateResponse(request, template_name, context)

def project_item(request, pk):
	template_name = 'archiveitem.html'

	item = Project.objects.get(pk=pk)

	context = {
		'item': item,
	}

	return TemplateResponse(request, template_name, context)

def publication(request):
	template_name = 'archivepublication.html'

	publications = Publication.objects.all()

	context = {
		'publications': publications,
	}

	return TemplateResponse(request, template_name, context)

def publication_item(request, pk):
	template_name = 'archiveitem.html'

	item = Publication.objects.get(pk=pk)

	context = {
		'item': item,
	}

	return TemplateResponse(request, template_name, context)

def book(request):
	template_name = 'archivebook.html'

	books = Book.objects.all()

	context = {
		'books':books,
	}

	return TemplateResponse(request, template_name, context)

def book_item(request, pk):
	template_name = 'archiveitem.html'

	item = Book.objects.get(pk=pk)

	context = {
		'item': item,
	}

	return TemplateResponse(request, template_name, context)