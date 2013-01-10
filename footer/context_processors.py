from models import Footer_Info, Footer_Logos
from django.conf import settings

def footer_text(request):
    footer_text = Footer_Info.objects.all()
    #footer_text = footer_texts.reverse()[0] 
    
    return {
        'footer_text': footer_text,
    }

def footer_logos(request):
    return {
        'footer_logos': Footer_Logos.objects.all().order_by('order'),
    }
