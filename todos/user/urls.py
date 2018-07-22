from django.conf.urls import url
from user import views

urlpatterns = [
    url(r'^login/', views.user_login, name='user_login'),
    url(r'^create/', views.create),
    url(r'^home/', views.home),
    url(r'^logout/', views.user_logout, name='user_logout')
]