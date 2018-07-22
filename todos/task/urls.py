from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.home),
    url(r'^create/', views.create),
    url(r'^list/', views.todo_list, name='todo_list'),
    url(r'^update/(?P<pk>[0-9]+)/$', views.todo_update, name='todo_update'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.todo_delete, name='todo_delete')
]