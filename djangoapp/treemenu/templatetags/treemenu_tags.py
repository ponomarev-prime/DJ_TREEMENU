from django import template
from django.urls import reverse

register = template.Library()

@register.simple_tag(takes_context=True)
def menu_links(context, menu_list):
    """
    Возвращает HTML-код для меню в виде ссылок на основе списка меню
    """
    html = ''
    for menu in menu_list:
        # Для каждого элемента списка генерируем ссылку
        url = reverse(menu.url_name, args=menu.url_args)
        html += f'<li><a href="{url}">{menu.name}</a></li>'
    return html
