#coding:utf-8


from lite.models import *
from django.forms.models import model_to_dict
from django.db.models import Sum
import json
from lib.gxgx_data import *

class ActionLogin():
    def __init__(self):
        pass

    '''
        @method 检验账号密码
    '''
    def check(self , username, password):
        return User.objects.filter(
            username = username,
            password = password,
        ).get().uuid

    '''
        @method 根据用户uuid 查询可以观看的数据范围
        @important
            list( xxx.values ) 将数据序列化！
    '''
    def get_broadcast_list(self,uuid):
        user =  User.objects.get( uuid = uuid )
        _broadcast_list = list( user.broadcast.all().values("id","name","tag","channel_id",'desc','range_time') )
        return _broadcast_list
        # print (  model_to_dict(_broadcast[0]) )
        # user.broadcase


if __name__  == '__main__':
    import django
    django.setup()
    e= ActionLogin()
    aa = e.get_broadcast_list("d64bcfc0-0bb9-11eb-9fb0-fcaa147ae146")
    print (aa)
    # print(e.get_broadcase_list("d64bcfc0-0bb9-11eb-9fb0-fcaa147ae146") )