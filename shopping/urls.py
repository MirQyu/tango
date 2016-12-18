from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^media/(?P<path>[0-9a-zA-z.]+)', views.image)
]