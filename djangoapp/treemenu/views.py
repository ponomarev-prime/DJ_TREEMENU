from django.shortcuts import render, get_object_or_404, redirect
from treemenu.models import Menu


def index_page(request):
    return render(request, "index.html")

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

def about_page(request):
    return render(request, "about.html")

def contact_page(request):
    return render(request, "contact.html")

def products_page(request):
    return render(request, "products.html")

def menu(request, menu_name):
    menu = Menu.objects.get(name=menu_name)
    items = menu.menuitem_set.all()
    context = {
        'items': items,
    }
    return render(request, 'treemenu/menu.html', context)