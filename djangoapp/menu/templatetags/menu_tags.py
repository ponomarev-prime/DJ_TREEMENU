from django import template
from django.urls import reverse
from menu.models import MenuItem

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    menu_items = MenuItem.objects.filter(name=menu_name).prefetch_related('menuitem_set')
    menu_html = '<ul>'
    for item in menu_items:
        menu_html += '<li'
        if request.path == item.url:
            menu_html += ' class="active"'
        menu_html += '><a href="{}">{}</a>'.format(reverse(item.url) if item.url.startswith('name:') else item.url, item.name)
        if item.menuitem_set.exists():
            menu_html += '<ul>'
            for subitem in item.menuitem_set.all():
                menu_html += '<li'
                if request.path.startswith(subitem.url):
                    menu_html += ' class="active"'
                menu_html += '><a href="{}">{}</a></li>'.format(reverse(subitem.url) if subitem.url.startswith('name:') else subitem.url, subitem.name)
            menu_html += '</ul>'
        menu_html += '</li>'
    menu_html += '</ul>'
    return menu_html
