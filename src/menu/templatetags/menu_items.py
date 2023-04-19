from django import template
from django.db.models import Prefetch

from blog.models import Categories
from menu.models import Menu

register = template.Library()


@register.inclusion_tag("menu/simple_menu.html")
def draw_menu(title):
    menu = (
        Menu.objects.filter(title=title)
        .prefetch_related("categories__child_category")
        .first()
    )
    return {"menu": menu}


@register.inclusion_tag("menu/submenu.html")
def sub_menu(menu_item):
    return {"sub_menu_items": (menu_item.child_category.all())}
