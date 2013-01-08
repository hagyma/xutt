from django.template.response import TemplateResponse

from menu.models import Menu
from models import Page

def index(request):
    template = 'index.html'

    try:
        main_page = Page.objects.get(menu__order=0)
    except:
        main_page = ''

    context = {
        'main_page': main_page
    }

    return TemplateResponse(request, template, context)
