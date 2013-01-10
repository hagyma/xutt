from models import Menu
from django.conf import settings

def menu_items(request):
    try:
        menus = Menu.objects.all().exclude(order=0).order_by('order')
    except:
        menus = ''
        
    return {
        'menu_items': menus ,
    }
