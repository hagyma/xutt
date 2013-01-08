from django.template.response import TemplateResponse
from django.http import HttpResponse

from models import Menu
from pages.models import Page

def show_menu_content(request, slug):
    template = 'page.html'

    menu_slug = slug

    try:
        page = Page.objects.get(menu__slug_en=slug)
    except:
        return HttpResponse('<h1>Page was found</h1>')

    context = {
        'page': page,
    }

    return TemplateResponse(request, template, context)
