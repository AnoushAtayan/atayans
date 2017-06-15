# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^stores/$', views.store_list, name='store_list'),
    url(r'^search results/$', views.store_search, name='store_search'),
    url(r'^stores/(?P<store_id>[1-9]+)$', views.store_detail, name='comments')

]