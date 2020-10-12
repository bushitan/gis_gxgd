#coding:utf-8

from django.views.generic import ListView
from django.shortcuts import render
from lib.message import *
# from .action.login import *
from .action.action import *
# action_episode = ActionEpisode()
from .models import *
class Index( ListView):
    template_name = 'index.html'
    context_object_name = 'article_list'

    def get_context_data(self, **kwargs):
        return super(Index, self).get_context_data(**kwargs)

    def get_queryset(self):
        pass

'''
    @method 收视人数
'''
class Hunan( ListView):
    template_name = 'gis_hunan.html'
    context_object_name = 'article_list'

    broadcast_id = ""
    def get(self, request, *args, **kwargs):
        self.broadcast_id = request.GET.get('broadcast_id',"")
        return super(Hunan, self).get(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        kwargs['gis'] = 123
        # kwargs['gis_list'] = [1,2,3]
        # address_list = Address.objects.filter(code=0)
        kwargs['channel_name'], kwargs['broadcast_name'] = action.episode.getName(self.broadcast_id)
        # kwargs['gis_list'], kwargs['max'], kwargs['min'] = action_episode.getCityCount(self.broadcast_id)
        kwargs['episode_list'],kwargs['episode_dict'] ,kwargs['max'] = action.episode.getCityList(self.broadcast_id)
        # print  (kwargs['gis_list'])
        return super(Hunan, self).get_context_data(**kwargs)

    def get_queryset(self):
        pass


'''
    @method 收视率
'''
class Rate( ListView):
    template_name = 'gis_rate.html'
    context_object_name = 'article_list'

    broadcast_id = ""
    def get(self, request, *args, **kwargs):
        self.broadcast_id = request.GET.get('broadcast_id',"")
        return super(Rate, self).get(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        # kwargs['gis'] = 123
        # kwargs['gis_list'] = [1,2,3]
        # address_list = Address.objects.filter(code=0)
        kwargs['channel_name'], kwargs['broadcast_name'] = action.episode.getName(self.broadcast_id)
        # kwargs['gis_list'], kwargs['max'], kwargs['min'] = action_episode.getCityCount(self.broadcast_id)
        kwargs['episode_list'],kwargs['episode_dict'] ,kwargs['max'] = action.episode.getRateCityList(self.broadcast_id)
        # print  (kwargs['gis_list'])
        return super(Rate, self).get_context_data(**kwargs)

    def get_queryset(self):
        pass


class UserLogin( ListView):
    def post(self, request, *args, **kwargs):
        username = request.POST.get("username","")
        password = request.POST.get("password","")
        _uuid = action.login.check( username ,password )
        _dict =   {
            "data":{
                "uuid":_uuid
            },
            "msg":"",
            "code": 0,
        }
        return HttpResponse( json.dumps( _dict ) ,content_type="application/json" )



class UserGetBroadcastList( ListView):
    def post(self, request, *args, **kwargs):
        uuid = request.POST.get("uuid","")
        _broadcast_list  = action.login.get_broadcast_list(uuid)
        _dict =   {
            "data":{
                "broadcast_list":_broadcast_list
            },
            "msg":"",
            "code": 0,
        }
        _json = json.dumps( _dict )
        return HttpResponse( _json ,content_type="application/json" )




# class Index1( ListView):
#     template_name = 'index.html'
#     context_object_name = 'article_list'
#
#     def get_context_data(self, **kwargs):
#         return super(Index1, self).get_context_data(**kwargs)
#
#     def get_queryset(self):
#         pass
#
#     def get(self, request, *args, **kwargs):
#         try:
#             print 111
#             print args
#             # print kwargs
#             # app =  kwargs.get('app',None)
#             # print app
#             _dict = {}
#             return MESSAGE_RESPONSE_SUCCESS(_dict)
#         except Exception as e :
#             a = Exception
#             print Exception
#             print e
#             return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )
#
#     def post(self, request, *args, **kwargs):
#         try:
#             _str_hash = request.POST['hash']
#             _dict = {
#                 'MSG':u'鐧诲綍鍒濆鍖栨垚鐙�',
#             }
#             return MESSAGE_RESPONSE_SUCCESS(_dict)
#         except Exception,e :
#             return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )
