from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.wod_index, name='wod_index'),
    url(r'^(?P<wod_id>[0-9]+)/$', views.wod_details, name='wod_details'),

]
