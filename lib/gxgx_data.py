#coding:utf-8

import time
import os
import requests
import json

class GXGDData():
	def __init__(self):
		self.cookie = ""
		self.login()

	# 请求参数
	def _post(self,url,data):
		headers = {
			'Cookie' :  self.cookie
		}
		r = requests.post(url, data=data, headers=headers)
		res = json.loads(r.content)
		return res

	#  登陆拿到cookie
	def login(self):
		url = "http://10.1.42.51:18089/StarV2/login.do"
		data ={
			'account': 'guest01',
			'passwd': '1234',
		}
		r = requests.post(url, data=data,)
		res = json.loads(r.content)
		self.cookie = r.headers._store['set-cookie'][1].split(";")[0] # 设置cookie
		# print(res)

	# 获取收视机顶盒数
	def get_stb_paly_num(self,**kwargs):
		url = 'http://10.1.42.51:18089/StarV2/live/getIndex.do'
		data = {
			'areaCode':kwargs['areaCode'] ,
			'groupFlag': 'false',
			'groupCode': 'GX001',
			'channelCodes':kwargs['channelCodes'] ,
			'dateRange':'%s:%s' % (kwargs['date'] ,kwargs['date'] ) ,# '2020-09-01:2020-09-01',
			'timeRange':'%s-%s' % (kwargs['startTime'] ,kwargs['endTime'] ) ,# '00:00:00-23:59:59',
			'dateInterval': 'f04', # f04按小时 ， f05 按天 ，f06按周，f07按月
			'indexName':'RTG000',
			'currentPage': '1',


			# areaCode: -1
			# groupFlag: false
			# groupCode: GX001
			# channelCodes: 445
			# dateRange: 2020-09-01:2020-09-01
			# timeRange: 00:00:00-00:10:00
			# dateInterval: f04
			# indexName: RTG000
			# currentPage: 1

			# 'areaCode': '0100',
			# 'groupFlag': 'false',
			# 'groupCode': 'GX001',
			# 'channelCodes': 445,
			# 'dateRange': '2020-09-01:2020-09-01',
			# 'timeRange': '00:00:00-00:10:00',
			# 'dateInterval': 'f04',
			# 'indexName': 'RTG000',
			# 'currentPage': 1,
		}
		res = self._post( url , data)
		print(res)
		print(res['contentList'][0]['valueList'][0])
		print(res['contentList'][0]['valueList'][0]['viewtime'])
		print(res['contentList'][0]['valueList'][0]['timeLong'])

		viewtime = res['contentList'][0]['valueList'][0]['viewtime']

		timeLong = res['contentList'][0]['valueList'][0]['timeLong']
		play = int (viewtime / timeLong)
		print (play)
		return play

if __name__ == '__main__':
	g = GXGDData()
	g.get_stb_paly_num(
		areaCode = '-1' ,
		channelCodes =  445,
		date = '2020-09-01',
		startTime = '00:00:00',
		endTime = '00:50:00',

	)
	# g.login()
#
#
# url = "http://123.207.38.251/dev/lite/print/get/wm_list/"
# data = {
# 	'token': 'bushitan',
# 	'start': start,
# 	'end': end,
# }
# r = requests.post(url, data=data)
# res = json.loads(r.content)
# wm_list =  res['data']['wm_list']