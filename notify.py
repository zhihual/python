#!/usr/bin/env python3
# -*- coding:utf-8 -*- 


import tushare as ts
from threading import Timer
import time
import smtplib  
from email.mime.text import MIMEText 
import datetime


quotelist = ['sh','sz','cyb','510050','510300','159915','204001','131810','511880','511990','000725','150200','000656','002739']

log_last_fluction=[]


def_fluction_rate = 0.03

                         
share_gc001_ammount = 0
share_gc001_order_price = 1.685

share_r001_ammount = 0
share_r001_order_price = 1.685

share_511880_ammount = 0
share_511880_buy_price = 100.013

share_511990_ammount = 0
share_511990_buy_price = 100.013


share_150200_ammount = 0
share_150200_buy_price = 0.972


quote_freq = 10


bSendEmail = 1
bGlobalNotify = 1
bEachItemNotify=0

bIsCheckHighFluction=1
bIsCheckLowFluction=1




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


def myanalysis():
	#Query Quote --start
	#print('******************************************************************')
	df = ts.get_realtime_quotes(quotelist)
	mydf = df['code']
	df = df.drop(['open', 'bid', 'ask', 'amount','a2_p', 'a3_v','a3_p', 'a4_v', 'a5_v', 'a5_p','date', 'code',
               'b1_v', 'b2_p', 'b2_v', 'b2_p', 'b3_v', 'b4_v', 'b4_p','b5_v', 'b5_p', 'a1_v', 'a2_v', 'a4_p', 'b1_p', 'b3_p', 'a1_p','volume'], axis=1)
    
	
	df.insert(0,'code', mydf[:])
	mydispy = df.drop(['name'],axis=1)
	#print(mydispy)
	#Query Quote --end
	size = len(quotelist)
	
		
	i = 0
	bIsNeedSendEmail = 0
	sendtitle = ''
	sendcontext = ''
	for i in range(size): # 循环计算
		global def_fluction_rate
		bAddMsgInfo = 0
		this = df.loc[i]
		#print(this)
		preclose_price = float(this.pre_close)
		preclose_price = round(preclose_price,2)
		cur_price = this.price
		cur_price=float(cur_price)
		addon_context='addon: '
		direction = '+'

		# Get a datetime object
		now = datetime.datetime.now()
		timestamp ='%d:%d:%d' % (now.hour,now.minute, now.second)
		
		if((bIsCheckHighFluction==1)and(cur_price>preclose_price)):
			fluct_rate = (cur_price-preclose_price)/preclose_price
			fluct_rate = round(fluct_rate,4)
			direction = '+'
		if((bIsCheckLowFluction==1)and(preclose_price>cur_price)):
			fluct_rate = (preclose_price-cur_price)/preclose_price
			fluct_rate = round(fluct_rate,4)
			direction = '-'
	    
		# check是否需要计算实时成本
		if((this.code =='204001')and(share_gc001_ammount>0)): #GC001
			delta = (share_gc001_ammount*share_gc001_order_price/100/360)-(share_gc001_ammount*0.001/100)
			delta = round(delta, 2)
			addon_context = '%.2f %d sell price %.2f' % (delta, share_gc001_ammount, share_gc001_order_price)
			def_fluction_rate = 0.03
			fluct_rate = cur_price
		elif((this.code=='131810')and(share_r001_ammount>0)): #R001
			delta = (share_r001_ammount*hare_r001_order_price/100/360)-(share_r001_ammount*0.001/100)
			delta = round(delta, 2)
			addon_context = '%.2f %d' % (delta, share_r001_ammount)
			def_fluction_rate = 0.03
			fluct_rate = cur_price
		elif((this.code =='511880')and(share_511880_ammount>0)): #银华日利
			abs = share_511880_ammount*(share_511880_buy_price-cur_price)
			rate = abs*356/share_511880_ammount
			abs = round(abs,2)
			rate = round(rate, 2)
			addon_context = '%.2f %d %.2f' % (rate*100, share_511880_ammount, abs )
			def_fluction_rate = 0.025
			fluct_rate = rate
		elif((this.code =='511990')and(share_511990_ammount>0)): #华宝添益
			abs = share_511990_ammount*(share_511990_buy_price-cur_price)
			rate = abs*356/share_511990_ammount
			abs = round(abs,2)
			rate = round(rate, 2)
			addon_context = '%.2f %d %.2f' % (rate*100, share_511990_ammount, abs )
			def_fluction_rate = 0.025
			fluct_rate = rate
		elif((this.code =='150200')and(share_150200_ammount>0)): #分级A
			abs = share_150200_ammount*(share_150200_buy_price-cur_price)
			abs = round(abs,2)
			addon_context = '%d %.2f' % (share_150200_ammount, abs )
		
			
		if(bSendEmail==1):
			if(log_last_fluction[i]<fluct_rate):
				log_last_fluction[i] = fluct_rate
				if(fluct_rate>def_fluction_rate):
					bAddMsgInfo = 1
					bIsNeedSendEmail=1
		if(bAddMsgInfo==1):
			sendtitle = '%s code %s %s  Rate %s%.2f' % (timestamp, this.code,this['name'], direction,fluct_rate*100) 
			singlecontext = '(code %s %s Rate %s%.2f (Now)%.2f Close%.2f %s)'%(this.code,this['name'], direction,fluct_rate*100, cur_price, preclose_price, addon_context)
			sendcontext = sendcontext+ singlecontext
			if(bEachItemNotify==1):
				send_mail(mailto_list,sendtitle,singlecontext)
	
	if((bIsNeedSendEmail ==1) and(bGlobalNotify==1)):
		print('send mail')
		send_mail(mailto_list,sendtitle,sendcontext)
		bIsNeedSendEmail = 0	
    
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
	time.sleep(100)
	#print('canstart', canstart)
	if(canstart==1):
		t.start()
		canstart = 0
#myanalysis()