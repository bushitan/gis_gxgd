# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import *

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
    pass
admin.site.register(Address,AddressAdmin)

class ChannelAdmin(admin.ModelAdmin):
    pass
admin.site.register(Channel,ChannelAdmin)

class BroadcastAdmin(admin.ModelAdmin):
    pass
admin.site.register(Broadcast,BroadcastAdmin)


class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('id','channel_name','boadcast','name','uv','pv','rate','address')
    # 显示频道名称
    def channel_name(self, obj):
        return u'%s' % obj.boadcast.channel.name
    channel_name.short_description = u'频道'

    actions = ['copy_episode']
    def copy_episode(self, request, queryset):
        rows_updated = queryset.update(status=3) # queryset参数为选中的Story对象
        message_bit = "%s 篇文章" % rows_updated
        self.message_user(request, "%s 已成功标记为已发布状态." % message_bit)
    copy_episode.short_description = u'复制剧集数据'

admin.site.register(Episode,EpisodeAdmin)