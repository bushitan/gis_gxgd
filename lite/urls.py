# -*- coding: utf-8 -*-


from django.conf.urls import url
from .views import *



urlpatterns = [

    url(r'^index/$', Index.as_view()),

    url(r'^gis/hunan/$', Hunan.as_view()),
    url(r'^gis/login/$', UserLogin.as_view()), #登陆
    url(r'^gis/user/broadcast_list/$', UserGetBroadcastList.as_view()), #获取直播数据列表


    # url('^index/(\d*)/callback/$',Index1.as_view()),

    # url(r'^tag/delete/$', TagAdd.as_view()),
    # url(r'^tag/get_list/$', TagAdd.as_view()),
    # url(r'^tag/update/$', TagAdd.as_view()),
]