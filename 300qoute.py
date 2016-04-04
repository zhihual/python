#!/usr/bin/env python3
# -*- coding:utf-8 -*- 


#!/usr/bin/env python3
# -*- coding:utf-8 -*- 


import tushare as ts
from threading import Timer
import time
import datetime

#'510310','510360','159924','159925','159927', small voluem 300 ETF
#'510430','510710', small 50ETF
#'159921',
#'513600','513660',
#,'159926'
#'159934','518800',
#'159920','513100','513500','159941','513030',
#'511210','511220',
#'159937',
#quotelist = ['510300','510330','159919','510050','159915','159902','510500','510900','511010','518880','511990','511810','511800','511880','150200','000725']

quotelist = ['510300','160615','160706','160807','165309','167901','163407','166007',]

log_last_fluction=[]

def_fluction_rate = 3.0





# log start time


def getcurtime():
	mtime = datetime.datetime.now()
	timestr ='%d:%d:%d:%d' % (mtime.day, mtime.hour, mtime.minute, mtime.second)
	return timestr

#debug information
startime=getcurtime


def getdebuginfo():
	logdump='Log dump:<br>'
	f=0
	fsize = len(quotelist)
	for f in range(fsize):
		logdump = logdump+'%s:%s <br>'%(quotelist[f],log_last_fluction[f])
	return logdump

def myanalysis():
	#Query Quote --start

	df = ts.get_realtime_quotes(quotelist)
	mydf = df['code']
	df = df.drop(['bid', 'ask', 'a2_p', 'a3_v','a3_p', 'a4_v', 'a5_v', 'a5_p','date', 'code',
               'b1_v', 'b2_p', 'b2_v', 'b2_p', 'b3_v', 'b4_v', 'b4_p','b5_v', 'b5_p', 'a1_v', 'a2_v', 'a4_p', 'b1_p', 'b3_p', 'a1_p'], axis=1)
    
	
	df.insert(0,'code', mydf[:])
	mydispy = df.drop(['name'],axis=1)
	#print(mydispy)
	#Query Quote --end
	size = len(quotelist)
	
	# Get a datetime object
	now = datetime.datetime.now()
	timestamp ='%d:%d:%d' % (now.hour,now.minute, now.second)
		
	
	for i in range(size): # 循环计算
		global def_fluction_rate
		bAddMsgInfo = 0
		this = df.loc[i]
		#print(this)
		open_price = float(this.pre_close) #### notice change to preclose
		open_price = round(open_price,3)
		cur_price = this.price
		cur_price=float(cur_price)
		cur_price= round(cur_price,3)
		addon_context='addon: '
		direction = '+'

	
		if (this.code == '204001' or this.code =='131810'):
			fluct_rate = cur_price
			def_fluction_rate = 3
		elif((this.code == '511880') or (this.code == '511990') or (this.code == '511800') or (this.code == '511810')):
			def_fluction_rate = 0.005
			if(cur_price>=open_price):
				fluct_rate = cur_price-open_price
				fluct_rate = round(fluct_rate,3)
				direction = '+'
			if(open_price>cur_price):
				fluct_rate = open_price - cur_price
				fluct_rate = round(fluct_rate,3)
				direction = '-'
		else:
			def_fluction_rate = 3
			if(cur_price == 0):
				fluct_rate=0
				direction='*'
			elif(cur_price>=open_price):
				fluct_rate = (cur_price-open_price)/open_price
				fluct_rate = round(fluct_rate,3)
				fluct_rate = fluct_rate*100
				fluct_rate = round(fluct_rate,3)
				direction = '+'
			elif(open_price>cur_price):
				fluct_rate = (open_price-cur_price)/open_price
				fluct_rate = round(fluct_rate,3)
				fluct_rate = fluct_rate*100
				fluct_rate = round(fluct_rate,3)
				direction = '-'
	    
		#print(log_last_fluction[i], fluct_rate, def_fluction_rate)
		if(log_last_fluction[i]<fluct_rate):
			log_last_fluction[i] = fluct_rate

							
		print('%s %s%-6.3f Now %-7.3f Preclose %-7.3f %s%-8.3f vol %10.3f(W) amount %11.3f(W) %-20s'%(this.code, direction,fluct_rate, cur_price, open_price,direction,log_last_fluction[i],round(float(this['volume'])/10000,3),round(float(this['amount'])/10000,3),this['name']))	
	


j=0
listsize = len(quotelist)
for j in range(listsize):
	log_last_fluction.append(0)

myanalysis()