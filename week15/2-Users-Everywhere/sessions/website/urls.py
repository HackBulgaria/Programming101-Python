from django.conf.urls import url

from .views import home, register, login, logout


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^profile$', home, name='profile'),
    url(r'^register$', register, name='register'),
    url(r'^login$', login, name='login'),
    url(r'^logout$', logout, name='logout'),
]
