from django import template

from menu.models import Menu

register = template.Library()

# @register.simple_tag
# def menu_items():
#     menu_items = Menu.objects.filter(parent__isnull=True)
#     return {'menu_items': menu_items}

@register.inclusion_tag('menu/simple_menu.html')
def draw_menu(title):
    menu = Menu.objects.filter(title=title).first()
    return {'menu': menu}


@register.inclusion_tag('menu/submenu.html')
def sub_menu(menu_item):
    return {'sub_menu_items': menu_item.child_category.all()}
