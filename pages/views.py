from django.template.response import TemplateResponse

from models import Page

def index(request):
    template = ''

    context = {

    }

    return TemplateResponse(request, template, context)
