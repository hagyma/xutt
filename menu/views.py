from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from models import Menu
from pages.models import Page

def show_menu_content(request, slug):
    template = 'page.html'

    menu_slug = slug

    page = get_object_or_404(Page, menu__slug_en=slug)

    context = {
        'page': page,
    }

    return TemplateResponse(request, template, context)
