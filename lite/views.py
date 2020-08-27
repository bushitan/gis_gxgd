#coding:utf-8

from django.views.generic import ListView
from lib.message import *
# from .action.login import *
from .models import *
class Index( ListView):
    template_name = 'index.html'
    context_object_name = 'article_list'

    def get_context_data(self, **kwargs):
        return super(Index, self).get_context_data(**kwargs)

    def get_queryset(self):
        pass

class Hunan( ListView):
    template_name = 'gis_hunan.html'
    context_object_name = 'article_list'

    def get_context_data(self, **kwargs):
        kwargs['gis'] = 123
        # kwargs['gis_list'] = [1,2,3]
        kwargs['gis_list'] = Episode.objects.all()

        return super(Hunan, self).get_context_data(**kwargs)

    def get_queryset(self):
        pass





    # def get(self, request, *args, **kwargs):
    #     try:
    #         print 11111
    #         _s_js_code = request.GET.get('js_code',"")
    #         _s_session = request.GET.get('session',"")
    #         _login = ActionLogin()
    #         _login.CheckSession(_s_js_code,_s_session)
    #         _dict = {
    #             'MSG':u'鐧诲綍鍒濆鍖栨垚鐙�',
    #         }
    #         print _dict
    #         return MESSAGE_RESPONSE_SUCCESS(_dict)
    #     except Exception as e :
    #         a = Exception
    #         print Exception
    #         print e
    #         return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

    def post(self, request, *args, **kwargs):
        try:
            _str_hash = request.POST['hash']
            _dict = {
                'MSG':u'鐧诲綍鍒濆鍖栨垚鐙�',
            }
            return MESSAGE_RESPONSE_SUCCESS(_dict)
        except Exception,e :
            return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )





class Index1( ListView):
    template_name = 'index.html'
    context_object_name = 'article_list'

    def get_context_data(self, **kwargs):
        return super(Index1, self).get_context_data(**kwargs)

    def get_queryset(self):
        pass

    def get(self, request, *args, **kwargs):
        try:
            print 111
            print args
            # print kwargs
            # app =  kwargs.get('app',None)
            # print app
            _dict = {}
            return MESSAGE_RESPONSE_SUCCESS(_dict)
        except Exception as e :
            a = Exception
            print Exception
            print e
            return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

    def post(self, request, *args, **kwargs):
        try:
            _str_hash = request.POST['hash']
            _dict = {
                'MSG':u'鐧诲綍鍒濆鍖栨垚鐙�',
            }
            return MESSAGE_RESPONSE_SUCCESS(_dict)
        except Exception,e :
            return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )
