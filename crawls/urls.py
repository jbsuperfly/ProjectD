from django.conf.urls import url
from . import views

app_name = 'crawls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/', views.home, name='home'),
    url(r'^through_the_tubes/', views.search_url, name='search_url'),
    url(r'^deeper_through_the_tubes/', views.search_deeper, name='search_deeper'),
    url(r'^matrix/', views.search_deepest, name='search_deepest'),
]
