#!/usr/bin/env python3
# -*- coding:utf-8 -*- 


#!/usr/bin/env python3
# -*- coding:utf-8 -*- 


import tushare as ts
from threading import Timer
import time
import datetime




quotelist = ['510300','159915','510500','204001','511880','000725','150200','162411','518880'] 
#,'161033','161227','160806','161706','160512'

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
	df = df.drop(['bid', 'ask', 'amount','a2_p', 'a3_v','a3_p', 'a4_v', 'a5_v', 'a5_p','date', 'code',
               'b2_p', 'b2_v', 'b2_p', 'b3_v', 'b4_v', 'b4_p','b5_v', 'b5_p', 'a2_v', 'a4_p', 'b3_p', 'volume'], axis=1)
    
	
	#df = df.drop(['bid', 'ask', 'amount','a2_p', 'a3_v','a3_p', 'a4_v', 'a5_v', 'a5_p','date', 'code',
    #           'b1_v', 'b2_p', 'b2_v', 'b2_p', 'b3_v', 'b4_v', 'b4_p','b5_v', 'b5_p', 'a1_v', 'a2_v', 'a4_p', 'b1_p', 'b3_p', 'a1_p','volume'], axis=1)
	
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
		#print(i)
		open_price = float(this.pre_close) #### notice change to preclose
		open_price = round(open_price,3)
		cur_price = this.price
		cur_price=float(cur_price)
		cur_price= round(cur_price,3)
		addon_context='addon: '
		direction = '+'

		a1_p = float(this.a1_p)
		b1_p = float(this.b1_p)
		a1_p = round(a1_p,3)
		b1_p = round(b1_p,3)
		
		b1_v = float(this.b1_v)
		a1_v = float(this.a1_v)
		a1_vs_b1 = a1_v*100/b1_v
		a1_vs_b1 = int(a1_vs_b1)
		
	
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

							
		#print('%s %s%-6.3f Now %-8.3f Preclose %-8.3f %s'%(this.code, direction,fluct_rate, cur_price, open_price, log_last_fluction[i]))
		print('%s %s%-6.3f Now %-7.3f Preclose %-7.3f a1_p %-7.3f b1_p %-7.3f a:b %-5.0f'%(this.code, direction,fluct_rate, cur_price, open_price, a1_p, b1_p,a1_vs_b1))	
	


j=0
listsize = len(quotelist)
for j in range(listsize):
	log_last_fluction.append(0)

myanalysis()