#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

import tushare as ts
from threading import Timer
import time

def myanalysis():
	#Query Quote --start
	print('******************************************************************')
	df = ts.get_realtime_quotes(['510300','159915','000725','150200','511880','511990','204001','131810'])
	mydf = df['code']
	df = df.drop(['name','open', 'pre_close', 'bid', 'ask', 'amount','a2_p', 'a3_v','a3_p', 'a4_v', 'a5_v', 'a5_p','date', 'code',
               'b1_v', 'b2_p', 'b2_v', 'b2_p', 'b3_v', 'b4_v', 'b4_p','b5_v', 'b5_p', 'a1_v', 'a2_v', 'a4_p', 'b1_p', 'b3_p', 'a1_p','volume'], axis=1)

	df.insert(0,'code', mydf[:])
	print(df)
	#Query Quote --end
	print('******************************************************************')

	#Investment total
	Yinhuarili_Invest=130*10000
	GC001_Invest = 130*10000
	huabo_Invest=130*10000
	Total_Invest = GC001_Invest
	#order
	standard = 2.7
	high_stand=5.0
	gc001_sell=1.685

	yinhua_buy=100.555
	yinhua_sell=100.563

	huabo_buy=100.013
	huabo_sell=100.021

	#Query GC001
	df = ts.get_realtime_quotes(['204001'])
	mydf = df['code']
	df = df.drop(['name','open', 'pre_close', 'bid', 'ask', 'amount','a2_p', 'a3_v','a3_p', 'a4_v', 'a5_v', 'a5_p','date', 'code',
               'b1_v', 'b2_p', 'b2_v', 'b2_p', 'b3_v', 'b4_v', 'b4_p','b5_v', 'b5_p', 'a1_v', 'a2_v', 'a4_p', 'b1_p', 'b3_p', 'a1_p','volume'], axis=1)
	df.insert(0,'code', mydf[:])
	gc001_cur = df.price
	gc001_cur=float(gc001_cur[0])

	gc001_cur_return = (GC001_Invest*gc001_cur/100/360)-(GC001_Invest*0.001/100)
	gc001_cur_return = round(gc001_cur_return, 2)

	gc001_sell_return = (GC001_Invest*gc001_sell/100/360)-(GC001_Invest*0.001/100)
	gc001_sell_return = round(gc001_sell_return, 2)

	print('GC001','Cur_Return', gc001_cur_return,'Cur',gc001_cur,'%')

	# GC001 end

	#yinhuarili
	df = ts.get_realtime_quotes(['511880'])
	mydf = df['code']
	df = df.drop(['name','open', 'pre_close', 'bid', 'ask', 'amount','a2_p', 'a3_v','a3_p', 'a4_v', 'a5_v', 'a5_p','date', 'code',
               'b1_v', 'b2_p', 'b2_v', 'b2_p', 'b3_v', 'b4_v', 'b4_p','b5_v', 'b5_p', 'a1_v', 'a2_v', 'a4_p', 'b1_p', 'b3_p', 'a1_p','volume'], axis=1)
	df.insert(0,'code', mydf[:])
	yinhua_cur = df.price
	yinhua_cur = float(yinhua_cur[0])

	share = Yinhuarili_Invest

	yinhuaret=share/yinhua_buy*(yinhua_cur-yinhua_buy)
	yinhua_ret_cur_abs = round(yinhuaret,2)
	yinhua_ret_cur_year =yinhuaret*365/share*100
	yinhua_ret_cur_year = round(yinhua_ret_cur_year,2)

	yinhuaret=share/yinhua_buy*(yinhua_sell-yinhua_buy)
	yinhua_ret_order_abs = round(yinhuaret,2)
	yinhua_ret_order_year =yinhuaret*365/share*100
	yinhua_ret_order_year = round(yinhua_ret_order_year,2)
	print('yinhua_ret_cur_abs', yinhua_ret_cur_abs, 'yinhua_ret_cur_year:',yinhua_ret_cur_year,'%')

#huabaotianyi

	df = ts.get_realtime_quotes(['511990'])
	mydf = df['code']
	df = df.drop(['name','open', 'pre_close', 'bid', 'ask', 'amount','a2_p', 'a3_v','a3_p', 'a4_v', 'a5_v', 'a5_p','date', 'code',
               'b1_v', 'b2_p', 'b2_v', 'b2_p', 'b3_v', 'b4_v', 'b4_p','b5_v', 'b5_p', 'a1_v', 'a2_v', 'a4_p', 'b1_p', 'b3_p', 'a1_p','volume'], axis=1)
	df.insert(0,'code', mydf[:])
	huabo_cur = df.price
	huabo_cur = float(huabo_cur[0])
	share = huabo_Invest

	huaboret=share/huabo_buy*(huabo_cur-huabo_buy)
	huabo_ret_cur_abs = round(huaboret,2)
	huabo_ret_cur_year =huaboret*365/share*100
	huabo_ret_cur_year = round(huabo_ret_cur_year,2)

	huaboret=share/huabo_buy*(huabo_sell-huabo_buy)
	huabo_ret_order_abs = round(huaboret,2)
	huabo_ret_order_year =huaboret*365/share*100
	huabo_ret_order_year = round(huabo_ret_order_year,2)
	print('huabo_ret_cur_abs', huabo_ret_cur_abs, 'huabo_ret_cur_year:',huabo_ret_cur_year,'%')

#Caculate Today's cash return rate
#CashRet = gc001_sell_return+yinhua_ret_order_abs
	CashRet = gc001_sell_return+huabo_ret_order_abs
	CashRate = CashRet*365/Total_Invest*100
	CashRate = round(CashRate,2)

	standardcash= Total_Invest*standard/100/365
	standardcash=round(standardcash,2)

	high_standardcash= Total_Invest*high_stand/100/365
	high_standardcash=round(high_standardcash,2)

	print('-----------------------------------------')
	#print('GC001','Sell_Order_Return',gc001_sell_return,'Sell_Order', gc001_sell,'%')
	#print('yinhua_ret_order_abs', yinhua_ret_order_abs, 'yinhua_ret_order_year:',yinhua_ret_order_year,'%')
	#print('huabo_ret_order_abs', huabo_ret_order_abs, 'huabo_ret_order_year:',huabo_ret_order_year,'%')

	
	print('CashRet',CashRet,'CashRate',CashRate,'%')
	print('StandardCash', standardcash, 'standard',standard,'%')
	#print('high_standardcash', high_standardcash, 'high_stand',high_stand,'%')
	print('******************************************************************')
	global canstart
	canstart = 1
#end analysis function
	
timer_interval = 1
canstart = 1

def delayrun():
	print('running')
	global canstart
	canstart = 1
	#print('change canstart', canstart)

while True:
	t = Timer(timer_interval,myanalysis)
	time.sleep(20)
	#print('canstart', canstart)
	if(canstart==1):
		t.start()
		canstart = 0
		
	#print('main running')
