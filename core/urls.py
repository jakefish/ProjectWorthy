from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.wod_index, name='wod_index'),


]
