#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

import tushare as ts
from threading import Timer
import time

import smtplib  
from email.mime.text import MIMEText  

mailto_list=["7275337@qq.com","dikehua@sina.com"] 
mail_host="smtp.sina.com"  #设置服务器 smtp.sina.com
mail_user="dikehua"    #用户名
mail_pass="7275337"   #口令 
mail_postfix="sina.com"  #发件箱的后缀
  
def send_mail(to_list,sub,content):  #to_list：收件人；sub：主题；content：邮件内容
    me="stock"+"<"+mail_user+"@"+mail_postfix+">"   #这里的hello可以任意设置，收到信后，将按照设置显示
    msg = MIMEText(content,_subtype='html',_charset='gb2312')    #创建一个实例，这里设置为html格式邮件
    msg['Subject'] = sub    #设置主题
    msg['From'] = me  
    msg['To'] = ";".join(to_list)  
    try:  
        s = smtplib.SMTP()  
		#s.set_debuglevel(1)
        s.connect(mail_host,587)  #连接smtp服务器
        s.login(mail_user,mail_pass)  #登陆服务器
        s.sendmail(me, to_list, msg.as_string())  #发送邮件
        s.close()  
        return True  
    except Exception as e:  
        print(str(e))
        return False  


pre_huabo_ret_cur_year = 0	
pre_yinhua_ret_cur_year = 0
pre_gc001_cur = 0
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
	global canstart
	global runtime
	runtime=runtime+1
	
	sendemail=0
	huaboinfo= '511990 Call:%.3f Rate:%.3f Abs:%.2f' % (huabo_cur, huabo_ret_cur_year,  huabo_ret_cur_abs)
	yinhuainfo='511880 Call:%.3f Rate:%.3f Abs:%.2f' % (yinhua_cur, yinhua_ret_cur_year,  yinhua_ret_cur_abs)
	gc001info='204001 Call:%.3f Rate:%.3f Abs:%.2f' %(gc001_cur, gc001_cur,gc001_cur_return)
	
	global pre_huabo_ret_cur_year
	global pre_yinhua_ret_cur_year
	global pre_gc001_cur
#only report on highest 	
	if(huabo_ret_cur_year>4.0):
		if(pre_huabo_ret_cur_year < huabo_ret_cur_year):
			stockinfo = huaboinfo
			sendemail=1
			pre_huabo_ret_cur_year = huabo_ret_cur_year
	elif(yinhua_ret_cur_year>4.0):
		if(pre_yinhua_ret_cur_year < yinhua_ret_cur_year):
			stockinfo = yinhuainfo
			sendemail=1
			pre_yinhua_ret_cur_year < yinhua_ret_cur_year
	elif(gc001_cur>4.0):
		if(pre_gc001_cur!=gc001_cur):
			stockinfo=gc001info
			sendemail=1
			pre_gc001_cur=gc001_cur
#notify include, timestamp, each number. 		
	if(sendemail == 1):
		sendtitle = '%s' % stockinfo 
		sendcontext = '(%s) (%s) (%s)'%(huaboinfo,yinhuainfo,gc001info)
		
	if(sendemail==1):
		print('send mail', )
		send_mail(mailto_list,sendtitle,sendcontext)
	print('****************************************************************',runtime)
	canstart = 1
	
#end analysis function
	
timer_interval = 1
canstart = 1
runtime = 0;



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
#myanalysis()