from django.template.response import TemplateResponse

from models import Menu
from pages.models import Page

def show_menu_content(request, slug):
    template = 'pages/page.html'

    context = {

    }

    return TemplateResponse(request, template, context)
