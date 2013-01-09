from models import Footer_Info, Footer_Logos
from django.conf import settings

def footer_text(request):
    return {
        'footer_text': Footer_Info.objects.all(),
    }

def footer_logos(request):
    return {
        'footer_logos': Footer_Logos.objects.all(),
    }
