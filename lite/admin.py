# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import *
import random
from lib.gxgx_data import *
import json

from .action.action_episode import *
action_episode = ActionEpisode()

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
    list_display = ('id','name','channel','username','password',)
    raw_id_fields = ('channel',)
    filter_horizontal = ('broadcast',)
    list_editable = ( 'username','password',)
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

    actions = ['add_rate','add_stb_arrive_count','add_stb_view_count']

    # 节目收视率
    def add_rate(self, request, queryset):
        count = action_episode.get_rate(queryset[0])
        self.message_user(request, "已经添加多少条数据。 %s." % count)
    add_rate.short_description = u'添加收视率'

    # 机顶盒到达数
    def add_stb_arrive_count(self, request, queryset):
        count = action_episode.get_stb_arrive_count(queryset[0])
        self.message_user(request, "已经添加多少条数据。 %s." % count)
    add_stb_arrive_count.short_description = u'添加剧集顶盒数到达数'

    # 收视机顶盒数
    def add_stb_view_count(self, request, queryset):
        count = action_episode.get_stb_view_count(queryset[0])
        self.message_user(request, "已经添加多少条数据。 %s." % count)
    add_stb_view_count.short_description = u'添加剧集收视机顶盒数'



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