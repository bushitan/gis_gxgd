#coding:utf-8


from lite.models import *
from django.db.models import Sum
import json
from lib.gxgx_data import *

class ActionEpisode():
	def __init__(self):
		pass

	def getSheng(self):
		pass

	# method 根据节目，获取各个地区数据
	def getCityCount(self,broadcast_id=2):
		# return Address.objects.filter(tag = 0)

		_address_list = Address.objects.filter(tag = 0)
		_address_data = []
		_max = 0
		_min = 0
		for address in _address_list:
			_sum = Episode.objects.filter(
				broadcast_id = broadcast_id,
				address = address
			).aggregate(number_of_uv = Sum('uv'))
			_count = _sum['number_of_uv'] 

			#计算最大值
			if _max < _count:
				_max = _count
			if _min < _count:
				_min = _count

			_address_data.append({"count":_count,"lat":address.latitude,"lng":address.longitude})
		return _address_data ,_max , _min
		# pass

	# method 根据节目，获取各个地区数据
	def getCityList(self,broadcast_id=2):
		# return Address.objects.filter(tag = 0)
		broadcast = Broadcast.objects.get(id = broadcast_id)
		# print( json.loads( broadcast.episode_list) )
		episode_list = json.loads( broadcast.episode_list)

		_dict = {}
		for e in episode_list:
			filter = Episode.objects.filter(broadcast_id = broadcast_id, code = e['code'])
			_dict[e['code']] = self._filter_2_list(filter)
		return episode_list,_dict

	def _filter_2_list(self,filter):
		_list = []
		for i in filter:
			_list.append({
				"count":i.uv,
				"lat":i.address.latitude,"lng":i.address.longitude
			})
		return _list

	'''
		@method 顶盒数到达数
	'''
	def get_stb_arrive_count(self,broadcast):
		gxgd = GXGDData() #获取大数据数据
		broadcast = broadcast
		episode_list = json.loads (broadcast.episode_list)
		address_list = Address.objects.filter( tag=0)
		count = 0
		for  episode in episode_list:
			for address in address_list:
				print ( episode)
				print ( episode['start_time'])
				print ( address.area_code)
				res = gxgd.get_stb_view_num(
					areaCode = address.area_code ,
					channelCodes =  445,
					date =   episode['date'],
					startTime =episode['start_time'],
					endTime = episode['end_time'],
					dateInterval = "f05",
					indexName = "REACH000",
				)
				distinct = res['contentList'][0]['valueList'][0]['distinct']
				uv = distinct
				e = Episode(
					broadcast = broadcast,
					address = address,
					name =  episode['name'],
					code =  episode['code'],
					start_time ="%s %s" %( episode['date'] , episode['start_time'] ),
					end_time ="%s %s" %( episode['date'] , episode['end_time'] ) ,
					uv = uv,
				)
				e.save()
				count = count + 1
		return count

	'''
		@method 获取收视机顶盒数
	'''
	def get_stb_view_count(self,broadcast):
		gxgd = GXGDData() #获取大数据数据

		# 数据存储
		broadcast = broadcast
		episode_list = json.loads (broadcast.episode_list)
		address_list = Address.objects.filter( tag=0)
		count = 0
		for  episode in episode_list:
			for address in address_list:
				print ( episode)
				print ( episode['start_time'])
				print ( address.area_code)
				res = gxgd.get_stb_view_num(
					areaCode = address.area_code ,
					channelCodes =  445,
					date =   episode['date'],
					startTime =episode['start_time'],
					endTime = episode['end_time'],
					dateInterval = "f04",
					indexName = "RTG000",
				)
				viewtime = res['contentList'][0]['valueList'][0]['viewtime']
				timeLong = res['contentList'][0]['valueList'][0]['timeLong']
				uv = int (viewtime / timeLong)
				e = Episode(
					broadcast = broadcast,
					address = address,
					name =  episode['name'],
					code =  episode['code'],
					start_time ="%s %s" %( episode['date'] , episode['start_time'] ),
					end_time ="%s %s" %( episode['date'] , episode['end_time'] ) ,
					uv = uv,
				)
				e.save()
				count = count + 1
		return count

if __name__  == '__main__':
	import django
	django.setup()
	e= ActionEpisode()
	print(e.getCityList())