from django.shortcuts import render, get_object_or_404, redirect
from treemenu.models import MenuItem
from .forms import MenuItemForm


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

def about_page(request):
    return render(request, "about.html")

def contact_page(request):
    return render(request, "contact.html")

def menu_list(request):
    menus = MenuItem.objects.all()
    return render(request, 'treemenu/menu_list.html', {'menus': menus})

def menu_detail(request, menu_id):
    menu = get_object_or_404(MenuItem, pk=menu_id)
    return render(request, 'treemenu/menu_detail.html', {'menu': menu, 'menu_id': menu_id})

def menu_edit(request, menu_id=None):
    if menu_id:
        menu = get_object_or_404(MenuItem, pk=menu_id)
    else:
        menu = MenuItem()

    if request.method == 'POST':
        form = MenuItemForm(request.POST, instance=menu)
        if form.is_valid():
            menu = form.save()
            return redirect('menu_detail', menu_id=menu.id)
    else:
        form = MenuItemForm(instance=menu)

    return render(request, 'treemenu/edit_menu_item.html', {'form': form})