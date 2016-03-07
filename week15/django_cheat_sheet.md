# Django Cheatsheet

## Start a Django project

You need Django installed - `$ pip install django`.

Then:

```
$ django-admin startproject <project_name>
```

## Create Django app

Use `manage.py`:

```
$ python manage.py startapp <app_name>
```

## Urls

The basic structure is as folllows:

In your main Django app, your `urls.py` should look like this:

```python
from django.contrib import admin
from django.conf.urls import include, url

from website import urls as website_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(website_urls)),
]
```

And in your `website` app (if you have one), `urls.py` should look like:

```python
from django.conf.urls import include, url

from .views import home

urlpatterns = [
  url(r'^$', home, name='home'),
]
```
