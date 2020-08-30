#coding:utf-8


from lite.models import *
from django.db.models import Sum


class ActionEpisode():
	def __init__(self):
		pass

	def getSheng(self):
		pass

	# method 根据节目，获取各个地区数据
	def getCity(self,broadcast_id):
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

if __name__  == '__main__':
	import django
	django.setup()
	e= ActionEpisode()
	print(e.getCity())