from django import template
from treemenu.models import MenuItem, Menu

register = template.Library()

@register.simple_tag
def draw_menu():
    menu = Menu.objects.all()
    if menu:
        return render_menu(menu)

def render_menu(menu):
    html = "<ul>"
    for item in menu:
        html += "<li>"
        html += f'<a href="#">{item.name}</a>'
        html += "</li>"
    html += "</ul>"
    return html