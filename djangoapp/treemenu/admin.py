from django.contrib import admin
from treemenu.models import MenuItem

# Register your models here.
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'url')

admin.site.register(MenuItem, MenuItemAdmin)