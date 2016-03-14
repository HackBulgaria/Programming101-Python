from django.conf.urls import url

from .views import index, panda

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^panda/$', panda, name='panda'),
]
