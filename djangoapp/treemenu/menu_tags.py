from django import template
from django.urls import reverse
from django.utils.safestring import mark_safe
from treemenu.models import MenuItem

register = template.Library()

def draw_menu(menu_name):
    """
    Draw a tree menu by menu_name
    """
    try:
        menu_items = MenuItem.objects.filter(menu_name=menu_name).order_by('tree_id', 'lft')
    except MenuItem.DoesNotExist:
        menu_items = []

    menu_html = "<ul>"
    for item in menu_items:
        menu_html += "<li>"
        url = item.url or reverse(item.named_url)
        active_class = "active" if item.is_active else ""
        menu_html += f'<a href="{url}" class="{active_class}">{item.label}</a>'
        menu_html += "</li>"
    menu_html += "</ul>"

    return mark_safe(menu_html)

register.simple_tag(draw_menu)
