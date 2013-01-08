from models import Menu
from django.conf import settings

def menu_items(request):
    return {
        'menu_items': Menu.objects.all(),
    }
