# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import *
import random
from lib.gxgx_data import *
import json
admin.site.site_header = u'广西广电网络频道分析平台'
admin.site.site_title = u'广西广电网络'

# # Register your models here.
# class MyAdminSite(admin.AdminSite):
#     site_header = u'好医生运维资源管理系统'  # 此处设置页面显示标题
#     site_title = u'好医生运维'  # 此处设置页面头部标题
#
# admin_site = MyAdminSite(name='management')
# admin_site = MyAdminSite(name='management')
# admin.site.register(User,UserAdmin)


class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(User,UserAdmin)

class AddressAdmin(admin.ModelAdmin):
    list_display = ('id','name','area_code','tag',)
    list_editable = ( 'area_code',)
    pass
admin.site.register(Address,AddressAdmin)

class ChannelAdmin(admin.ModelAdmin):
    pass
admin.site.register(Channel,ChannelAdmin)

class BroadcastAdmin(admin.ModelAdmin):

    actions = ['add_episode']

    # 添加剧集数据
    def add_episode(self, request, queryset):
        gxgd = GXGDData()

        # rows_updated = queryset.update(status=3) # queryset参数为选中的Story对象
        # message_bit = "%s 篇文章" % rows_updated
        # episode_list = list( queryset[0].episode_list)
        broadcast = queryset[0]
        episode_list = json.loads (broadcast.episode_list)
        address_list = Address.objects.filter( tag=0)
        # print(address_list)
        count = 0
        for  episode in episode_list:
            for address in address_list:
                print ( episode)
                print ( episode['start_time'])
                print ( address.area_code)
                uv = gxgd.get_stb_paly_num(
                    areaCode = address.area_code ,
                    channelCodes =  445,
                    date = '2020-09-01',
                    startTime =episode['start_time'],
                    endTime = episode['end_time'],
                )
                e = Episode(
                    broadcast = broadcast,
                    address = address,
                    name =  episode['name'],
                    code =  episode['code'],
                    start_time ="%s %s" %( episode['date'] , episode['start_time'] ),
                    end_time ="%s %s" %( episode['date'] , episode['end_time'] ) ,
                    uv = uv
                    # uv = 1
                )
                e.save()
                count = count + 1
        self.message_user(request, "已经添加多少条数据。 %s." % count)
    add_episode.short_description = u'添加剧集数据'

admin.site.register(Broadcast,BroadcastAdmin)


class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('id','channel_name','broadcast','name','code','uv','pv','rate','address')
    list_editable = ( 'uv','pv','rate',)
    # 显示频道名称
    def channel_name(self, obj):
        return u'%s' % obj.broadcast.channel.name
    channel_name.short_description = u'频道'

    actions = ['copy_episode']
    def copy_episode(self, request, queryset):
        rows_updated = queryset.update(status=3) # queryset参数为选中的Story对象
        message_bit = "%s 篇文章" % rows_updated
        self.message_user(request, "%s 已成功标记为已发布状态." % message_bit)
    copy_episode.short_description = u'复制剧集数据'

admin.site.register(Episode,EpisodeAdmin)