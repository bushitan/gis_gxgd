# -*- coding: utf-8 -*-
from lib.message import *
from lite.models import *

class SessionMiddleware(object):

	'''
		@method 判断是否post请求。。在post请求下，验证账号
	'''
	def process_request(self, request):
		#检查是否有session值传入
		#有，则判断是否存在

		# 如果为登陆，则不不需要验证
		# if request.path == u'/gis/user/broadcast_list/':
		# 	return

		# _uuid = ''
		# if request.method == 'GET':
		# 	_uuid = request.GET.get("uuid","")
		# 	return
		# 	# return
		# if request.method == 'POST':

		if request.path == u'/gis/user/broadcast_list/' or\
		   request.path == u'/gis/hunan/':
			_uuid = request.POST.get("uuid","")

			if  User.objects.filter( uuid = _uuid).exists() is False: #用户不存在
					return HttpResponse( json.dumps({
						"data":{},
						"msg":"用户不存在",
						"code":-1,
					} ),content_type="application/json" )
		return


	def process_response(self, request, response):
		# print "process_response"
		# if request.method == 'POST':
		# 	if response.content == '':
		# 		return response
        #
		# 	else:
		# 		# print ( type( json.loads(  response.content )))
		# 		# print (json.loads(  response.content ))
        #
		# 		_dict = json.loads(  response.content )
		# 		# json.dumps( _dict )
		# 		return HttpResponse( json.dumps( _dict ) ,content_type="application/json" )
		# 		# return HttpResponse( json.dumps( dict( response.content ) ),content_type="application/json" )
		# else:
			return response



# class SessionMiddleware(object):
# 	def process_request(self, request):
# 		#检查是否有session值传入
# 		#有，则判断是否存在
# 		_items = request.GET.dict()
# 		print("sessiong    123")
# 		if _items.has_key("session"):  	#session字段存在
# 			session = request.GET.get('session',"") #获取session
# 			if  User.objects.filter( session = session).exists() is False: #用户不存在
# 				if _items.has_key("js_code") is False: # js_code为登陆验证字段，若不存在，返回登陆失败
# 					return MESSAGE_RESPONSE_LOGIN_OUT()
# 		return
#
# 	def process_response(self, request, response):
# 		# print "process_response"
# 		return response
#
