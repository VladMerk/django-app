from django import template

from menu.models import MenuItem

register = template.Library()

@register.simple_tag
def menu_items():
    menu_items = MenuItem.objects.filter(parent__isnull=True)
    return {'menu_items': menu_items}

@register.inclusion_tag('menu/submenu.html')
def sub_menu(menu_item):
    return {'sub_menu_items': menu_item.children.all()}
