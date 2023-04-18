from django import template
from menu.models import MenuItem

register = template.Library()

# @register.simple_tag()
# def menu_tag():
#     return MenuItem.objects.all()

@register.simple_tag()
def menu_tag():
    # root_items = MenuItem.objects.filter(parent=None)
    root_items = MenuItem.objects.all()

    def build_menu_tree(items):
        item_dict = {}
        for item in items:
            item_dict[item.id] = {
                'item': item,
                'children': []
            }
        for item_id, item_info in item_dict.items():
            parent_id = item_info['item'].parent_id
            if parent_id:
                item_dict[parent_id]['children'].append(item_id)

        menu_tree = []
        for item_id, item_info in item_dict.items():
            if not item_info['item'].parent_id:
                menu_tree.append(item_info)

        return menu_tree

    menu_tree = build_menu_tree(root_items)
    return menu_tree
