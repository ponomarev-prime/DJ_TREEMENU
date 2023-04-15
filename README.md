![](gitcontent/djtreemenu.png)

# DJ TREE MENU | UPTRADER 

**Django + PostgreSQL + Adminer**

```
docker compose up --build

docker compose up
docker compose down
```

Достуы, их нужно скопировать в созданый файл `.env`:
```
DJ_ADM_L='admin'
DJ_ADM_P='admin'

DB_HOST='db'
DB_NAME='postgres'
DB_USER='postgres'
DB_PASSWORD='password'
```

## Задача

Нужно сделать django app, который будет реализовывать древовидное меню, соблюдая следующие условия:

1) Меню реализовано через template tag
2) Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.
3) Хранится в БД.
4) Редактируется в стандартной админке Django
5) Активный пункт меню определяется исходя из URL текущей страницы
6) Меню на одной странице может быть несколько. Они определяются по названию.
7) При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.
8) На отрисовку каждого меню требуется ровно 1 запрос к БД

Нужен django-app, который позволяет вносить в БД меню (одно или несколько) через админку, и нарисовать на любой нужной странице меню по названию.

`{% draw_menu 'main_menu' %}`

При выполнении задания из библиотек следует использовать только Django и стандартную библиотеку Python.

При решении тестового задания у вас не должно возникнуть вопросов. Если появляются вопросы, вероятнее всего, у вас недостаточно знаний. Задание выложить на гитхаб.



## Струкутра

`djangoapp` - main dgango app

`treemenu` - приложение которое реализует древовидное меню


Содержимаое корневой папки:

`djangoapp` - директория с Django приложением

`gitcontent` - директория с контентом для git, напримр для `README.md`

`venv` - директория с Python Virtual Environment

`.gitignore `- файл, который определяет, какие файлы и директории Git должен игнорировать при выполнении операций Git.

`djangotest.py` - тестовый файл для Django приложения

`README.md` - файл с описанием проекта, возможно, написанный на языке разметки Markdown.

`requirements.txt` - файл со списком зависимостей Python, которые нужны для запуска проекта.


## Конфигурирование

### STATIC
```
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```
```
python manage.py collectstatic
```
### PostgreSQL
```
pip install psycopg2
```
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("DB_NAME"),
        'USER': os.getenv("DB_USER"),
        'PASSWORD': os.getenv("DB_PASSWORD"),
        'HOST': os.getenv("DB_HOST"),
        'PORT': '5432',
    }
}
```

```
docker compose ps
NAME                    IMAGE               COMMAND                  SERVICE             CREATED              STATUS              PORTS
dj_treemenu-adminer-1   adminer             "entrypoint.sh php -…"   adminer             About a minute ago   Up About a minute   0.0.0.0:8080->8080/tcp
dj_treemenu-db-1        postgres:latest     "docker-entrypoint.s…"   db                  About a minute ago   Up About a minute   0.0.0.0:5432->5432/tcp
dj_treemenu-web-1       dj_treemenu-web     "python manage.py ru…"   web                 About a minute ago   Up About a minute   0.0.0.0:8000->8000/tcp
```

```
docker exec dj_treemenu-web-1 python manage.py makemigrations
docker exec dj_treemenu-web-1 python manage.py migrate

docker exec dj_treemenu-web-1 python manage.py createsuperuser
```

```
docker exec -it dj_treemenu-web-1 bash

python manage.py createsuperuser
```

### Добавление записей в БД 

```
PS C:\Users\ponom\Documents\CODE\DJ_TREEMENU> docker exec -it dj_treemenu-web-1 bash
root@3bc255dec306:/code# ls
__pycache__  djangoapp  manage.py  menu_data.py  static  templates  treemenu  venv
root@3bc255dec306:/code# python -V
Python 3.11.3
root@3bc255dec306:/code# python manage.py shell
```
`menu_data.py`:
```
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
    parent=None,
    url='/contact/'
)
```
### Добавление 404

`views.py`:
```
def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)
```
`urls.py`:
```
handler404 = "treemenu.views.page_not_found_view"
```

`djangoapp/templates/404.html`

## Решение

В моём случае в файле `base.html` есть вызов `{% menu_links menu_list %}` который отвечает за динамическую отрисовку меню. 

Пункты меню я создал вручную с помощью `djangoapp/menu_data.py` и админ-панели.