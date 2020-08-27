# -*- coding: utf-8 -*-


from django.conf.urls import url
from .views import *



urlpatterns = [

    url(r'^index/$', Index.as_view()),

    url(r'^gis/hunan/$', Hunan.as_view()),

    url('^index/(\d*)/callback/$',Index1.as_view()),

    # url(r'^tag/delete/$', TagAdd.as_view()),
    # url(r'^tag/get_list/$', TagAdd.as_view()),
    # url(r'^tag/update/$', TagAdd.as_view()),
]