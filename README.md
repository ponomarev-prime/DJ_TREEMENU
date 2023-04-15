![](gitcontent/djtreemenu.png)

# DJ TREE MENU | UPTRADER 

**Python + PostgreSQL + Adminer**

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
docker exec dj_treemenu-web-1 python manage.py makemigrations
docker exec dj_treemenu-web-1 python manage.py migrate

docker exec dj_treemenu-web-1 python manage.py createsuperuser
```

```
docker exec -it dj_treemenu-web-1 bash

python manage.py createsuperuser
```

## Решение

В моём случае в файле `base.html` есть вызов `{% menu_links menu_list %}` который отвечает за динамическую отрисовку меню. 

Пункты меню я создал вручную с помощью `djangoapp/menu_data.py` и админ-панели.