from abc import ABC, abstractmethod

class MenuComponent(ABC):
    @abstractmethod
    def draw(self):
        pass
    
    def add_component(self, component):
        pass
    
    def remove_component(self, component):
        pass
    
    def get_children(self):
        pass

class MenuItem(MenuComponent):
    def __init__(self, name, url):
        self.name = name
        self.url = url
        
    def draw(self):
        return f'<li><a href="{self.url}">{self.name}</a></li>'
        
class Menu(MenuComponent):
    def __init__(self, name):
        self.name = name
        self.children = []
        
    def draw(self):
        menu = f'<ul>{self.name}'
        for child in self.children:
            menu += child.draw()
        menu += '</ul>'
        return menu
    
    def add_component(self, component):
        self.children.append(component)
        
    def remove_component(self, component):
        self.children.remove(component)
        
    def get_children(self):
        return self.children

class MenuIterator:
    def __init__(self, menu):
        self.menu_stack = [menu.get_children()[::-1]]
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.menu_stack:
            raise StopIteration
            
        current_menu_items = self.menu_stack[-1]
        if not current_menu_items:
            self.menu_stack.pop()
            return next(self)
        
        next_item = current_menu_items.pop()
        if isinstance(next_item, Menu):
            self.menu_stack.append(next_item.get_children()[::-1])
            
        return next_item

class MenuFactory:
    def create_menu(self, name):
        return Menu(name)
    
    def create_menu_item(self, name, url):
        return MenuItem(name, url)
    
class MenuRenderer:
    def __init__(self, factory):
        self.factory = factory
        
    def render_menu(self, menu):
        menu_iterator = MenuIterator(menu)
        menu_html = f'<nav>{menu.draw()}</nav>'
        return menu_html