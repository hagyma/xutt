from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404

from menu.models import Menu
from models import Page

def index(request):
    template = 'index.html'

    main_page = get_object_or_404(Page, menu__order=0)

    context = {
        'main_page': main_page
    }

    return TemplateResponse(request, template, context)
