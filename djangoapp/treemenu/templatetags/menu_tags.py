from django import template
from treemenu.models import MenuItem, Menu

register = template.Library()

@register.simple_tag
def draw_menu(menu_id):
    menu = MenuItem.objects.filter(menu_id=menu_id).all()
    if menu:
        return render_menu(menu)

def render_menu(menu):


    html = "<ul>"
    for item in menu:
        html += "<li>"
        html += f'<a href="{item.url}">{item.name}</a>'
        if item:
            html += render_menu(item)
        html += "</li>"
    html += "</ul>"
    return html