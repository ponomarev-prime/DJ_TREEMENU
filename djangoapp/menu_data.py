from treemenu.models import MenuItem

# Создание первой записи
menu_item1 = MenuItem.objects.create(
    name='Home',
    parent=None,
    url='/'
)

# Создание второй записи
menu_item2 = MenuItem.objects.create(
    name='About',
    parent=None,
    url='/about/'
)

# Создание третьей записи, которая будет дочерней для первой
menu_item3 = MenuItem.objects.create(
    name='Contact',
    parent=menu_item1,
    url='/contact/'
)
