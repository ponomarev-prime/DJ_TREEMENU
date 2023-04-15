"""
URL configuration for djangoapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from treemenu.views import menu_list, menu_detail, menu_edit, about_page, contact_page, page_not_found_view


app_name = 'treemenu'

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", menu_list, name='menu_list'),
    path("details/<int:menu_id>/", menu_detail, name='menu_detail'),
    path("edit/<int:menu_id>/", menu_edit, name='menu_edit'),
    path("about/", about_page, name='about'),
    path("contact/", contact_page, name='contact')
]

handler404 = "treemenu.views.page_not_found_view"