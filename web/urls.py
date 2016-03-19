from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index_page, name='index'),
    url(r'^base/', views.base_page, name='base'),
]