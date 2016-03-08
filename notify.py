#!/usr/bin/env python3
# -*- coding:utf-8 -*- 


import tushare as ts
from threading import Timer
import time
import smtplib  
from email.mime.text import MIMEText 
import datetime

from tkinter import *
import tkinter.messagebox as messagebox


quotelist = ['510050','510300','159915','204001','131810','511880','511990','000725','150200','000656','002739']

log_last_fluction=[]

quote_freq =10
bSendEmail = 1
bGlobalNotify = 1
bEachItemNotify=0
mailoption=1  #1 email #2 message box

def_fluction_rate = 3.0

bNeedReset=0




# log start time


def getcurtime():
	mtime = datetime.datetime.now()
	timestr ='%d:%d:%d:%d' % (mtime.day, mtime.hour, mtime.minute, mtime.second)
	return timestr

#debug information
startime=getcurtime

mailto_list=["7275337@qq.com","dikehua@sina.com"] 
mail_host="smtp.sina.com"  #设置服务器 smtp.sina.com
mail_user="dikehua"    #用户名
mail_pass="7275337"   #口令 
mail_postfix="sina.com"  #发件箱的后缀
  
def send_mail(to_list,sub,content):  #to_list：收件人；sub：主题；content：邮件内容
    me="Message"+"<"+mail_user+"@"+mail_postfix+">"   #这里的hello可以任意设置，收到信后，将按照设置显示
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

def getdebuginfo():
	logdump='Log dump:<br>'
	f=0
	fsize = len(quotelist)
	for f in range(fsize):
		logdump = logdump+'%s:%s <br>'%(quotelist[f],log_last_fluction[f])
	return logdump

def myanalysis():
	#Query Quote --start
	print('******************************************************************')
	df = ts.get_realtime_quotes(quotelist)
	mydf = df['code']
	df = df.drop(['bid', 'ask', 'amount','a2_p', 'a3_v','a3_p', 'a4_v', 'a5_v', 'a5_p','date', 'code',
               'b1_v', 'b2_p', 'b2_v', 'b2_p', 'b3_v', 'b4_v', 'b4_p','b5_v', 'b5_p', 'a1_v', 'a2_v', 'a4_p', 'b1_p', 'b3_p', 'a1_p','volume'], axis=1)
    
	
	df.insert(0,'code', mydf[:])
	mydispy = df.drop(['name'],axis=1)
	#print(mydispy)
	#Query Quote --end
	size = len(quotelist)
	
	# Get a datetime object
	now = datetime.datetime.now()
	timestamp ='%d:%d:%d' % (now.hour,now.minute, now.second)
		
	#method to restart to send notify email
	global bNeedReset
	if((now.hour == 9) and (now.minute>29) and (now.minute<31)):
	#if((now.hour == 11) and (now.minute>9) and (now.minute<11)):
		if (bNeedReset==0):
			print('set flag')
			send_mail(mailto_list,'set_flag %s<br>'% getcurtime(),getdebuginfo())
			bNeedReset=1
	else:
		if(bNeedReset==1):
			k=0
			ksize = len(quotelist)
			for k in range(ksize):
				log_last_fluction[k]=0
			bNeedReset=0
			print('clar flag')
			send_mail(mailto_list,'clear flag %s<br>'%getcurtime(),getdebuginfo())
			
		
	i = 0
	bIsNeedSendEmail = 0
	sendtitle = ''
	sendcontext = ''
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
		elif((this.code == '511880') or (this.code == '511990')):
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
	    
		if(bSendEmail==1):
			#print(log_last_fluction[i], fluct_rate, def_fluction_rate)
			if(log_last_fluction[i]<fluct_rate):
				log_last_fluction[i] = fluct_rate
				if(fluct_rate>def_fluction_rate):
					#print('add',log_last_fluction[i], fluct_rate, def_fluction_rate)
					bAddMsgInfo = 1
					bIsNeedSendEmail=1
							
		print('%s %s %s%.3f Now%.3f Preclose%.3f'%(this.code,this['name'], direction,fluct_rate, cur_price, open_price))	
		if(bAddMsgInfo==1):
			sendtitle = '%s %s %s%.3f' % (timestamp, this.code, direction,fluct_rate) 
			singlecontext = '%s %s %s%.3f Now %.3f Preclose%.3f log%.3f <br>'%(this.code,this['name'], direction,fluct_rate, cur_price, open_price, log_last_fluction[i])
			sendcontext = sendcontext+ singlecontext
			if(bEachItemNotify==1):
				print('send')
				send_mail(mailto_list,sendtitle,singlecontext)
	
	if((bIsNeedSendEmail ==1) and(bGlobalNotify==1)):
		print('send mail')
		if(mailoption == 1):
			#print(sendcontext)
			sendcontext= sendcontext+getdebuginfo()
			send_mail(mailto_list,sendtitle,sendcontext)
		elif(mailoption==2):
		    messagebox.showinfo(sendtitle, sendcontext)
		
	bIsNeedSendEmail = 0
	sendtitle = 0
	sendcontext = 0
		
    
	global runtime
	runtime = runtime+1
	print('********************************************************',runtime,timestamp)
	global canstart
	canstart = 1

	
canstart = 1
runtime = 0


j=0
listsize = len(quotelist)
for j in range(listsize):
	log_last_fluction.append(0)
while True:
	t = Timer(quote_freq,myanalysis)
	time.sleep(10)
	#print('canstart', canstart)
	if(canstart==1):
		t.start()
		canstart = 0
#myanalysis()