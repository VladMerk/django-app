from django import template
from menu.models import MenuItem


register = template.Library()

@register.simple_tag()
def get_menu(menu_item):
    menu_items = MenuItem.objects.filter(title=menu_item)
    return build_menu_tree(menu_items)

def build_menu_tree(menu_items):
    menu_tree =[]
    menu_dict ={}

    for item in menu_items:
        menu_dict[item.id] = item

    for item in menu_items:
        if not item.parent_id:
            menu_tree.append(item)
        else:
            parent = menu_dict.get(item.parent_id)
            if parent:
                if not hasattr(parent, 'children'):
                    parent.children = []
                parent.children.append(item)
    return menu_tree
