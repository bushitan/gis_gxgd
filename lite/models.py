﻿# -*- coding: utf-8 -*-
from django.db import models
from lib.util import *
# Create your models here.
import django.utils.timezone as timezone
def day_365_hence(): #集点默认365天有效期
    return timezone.now() + timezone.timedelta(days=365)
import uuid
import pymysql

# 基础类 虚函数
class Base(models.Model):
    name = models.CharField(max_length=32, verbose_name=u'名字',default="",null=True,blank=True)
    admin_name = models.CharField(max_length=32, verbose_name=u'后台显示名字',default="",null=True,blank=True)
    uuid = models.CharField(max_length=36, verbose_name=u'uuid',default="",null=True,blank=True)
    create_time = models.DateTimeField(u'创建时间',default = timezone.now)
    class Meta:
        abstract = True
    def save(self, *args, **kwargs):
            # 创建用户时，生成唯一ID
            # print (self)
            if not self.uuid:
                self.uuid = str( uuid.uuid1())
            # if not self.short_uuid:
            #     # self.short_uuid = short_uuid_create(self.uuid)
            #     self.short_uuid = short_uuid_create(self.store.id,self.sn)
            super(Base,self).save(*args, **kwargs)

class User(Base):
    # models.ImageField()
    logo = models.CharField(max_length=300, verbose_name=u'logo',default="",null=True,blank=True)
    nick_name =  models.CharField(max_length=100, verbose_name=u'昵称',null=True,blank=True)
    wx_id =  models.CharField(max_length=100, verbose_name=u'微信id',null=True,blank=True)

    wx_open_id = models.CharField(max_length=50, verbose_name=u'微信OpenID',null=True,blank=True)
    wx_session_key = models.CharField( max_length=128,verbose_name=u'微信SessionKey',null=True,blank=True)
    wx_expires_in = models.FloatField( verbose_name=u'微信SessionKey',null=True,blank=True)
    session = models.CharField (max_length=128, verbose_name=u'session',null=True,blank=True)
    expires = models.FloatField( verbose_name=u'expires',null=True,blank=True)

    phone = models.CharField(max_length=40, verbose_name=u'电话',null=True,blank=True)
    class Meta:
        verbose_name_plural = verbose_name = u'用户'
    def __unicode__(self):
        return '%s' % (self.id)


# 区域
class Address(Base):
    father = models.ForeignKey('self', verbose_name=u'所属区域',null=True,blank=True)
    latitude =  models.FloatField( verbose_name=u'纬度',default=0,null=True,blank=True)
    longitude =  models.FloatField(  verbose_name=u'经度',default=0,null=True,blank=True)
    tag =  models.IntegerField( verbose_name=u'区域标签',default=0)
    class Meta:
        verbose_name_plural = verbose_name = u'区域'
    def __unicode__(self):
        return '%s' % (self.name)


# 频道
class Channel(Base):
    # phone = models.CharField(max_length=40, verbose_name=u'电话',null=True,blank=True)
    tag =  models.IntegerField( verbose_name=u'频道标签',default=0)
    class Meta:
        verbose_name_plural = verbose_name = u'1、频道'
    def __unicode__(self):
        return '%s' % (self.name)
# 节目
class Broadcast(Base):
    channel = models.ForeignKey(Channel, verbose_name=u'所属频道',null=True,blank=True)
    episode_list = models.TextField(  verbose_name=u'剧集时间表',null=True,blank=True)
    tag =  models.IntegerField( verbose_name=u'节目标签',default=0)
    class Meta:
        verbose_name_plural = verbose_name = u'2、节目'
    def __unicode__(self):
        return '%s' % (self.name)

# 剧集
class Episode(Base):
    boadcast = models.ForeignKey(Broadcast, verbose_name=u'所属节目',null=True,blank=True)
    address = models.ForeignKey(Address, verbose_name=u'所属区域',null=True,blank=True)
    rate =  models.FloatField( verbose_name=u'收视率',default=0)
    uv =  models.IntegerField( verbose_name=u'访问人数',default=0)
    pv =  models.IntegerField( verbose_name=u'访问次数',default=0)
    start_time = models.DateTimeField(u'开始时间',default = timezone.now)
    end_time = models.DateTimeField(u'结束时间',default = timezone.now)
    tag =  models.IntegerField( verbose_name=u'剧集标签',default=0)

    # nick_name =  models.CharField(max_length=100, verbose_name=u'昵称',null=True,blank=True)
    # phone = models.CharField(max_length=40, verbose_name=u'电话',null=True,blank=True)
    class Meta:
        verbose_name_plural = verbose_name = u'3、剧集'
    def __unicode__(self):
        return '%s' % (self.name)



