#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

import json
#import re
try:
	from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

import tushare as ts
	
con_redeem = -0.9
#con_redeem = 10

myreq = Request('http://www.jisilu.cn/data/lof/stock_lof_list/?___t=1459332174309')
myreq.add_header("Accept-Language", "en-US,en;q=0.5")
myreq.add_header("Connection", "keep-alive")	
myreq.add_header('Referer', "http://www.jisilu.cn/")
myreq.add_header("User-Agent", 'Mozilla/5.0 (Windows NT 6.1; rv:37.0) Gecko/20100101 Firefox/37.0')
lines = urlopen(myreq, timeout = 10).read()
js = json.loads(lines.decode('utf-8'))
lof_list=js['rows']
i=0
for i in range(len(lof_list)):
	mydicts=lof_list[i]
	subdict=mydicts['cell']
	discount_rt = float(subdict['discount_rt'][:-1])
	

	
	if(discount_rt < con_redeem):
		df = ts.get_realtime_quotes(subdict['fund_id'])
		this = df.loc[0]
		a1_p = float(this.a1_p)
		nav = float(subdict['fund_nav'])
		real_rt = 0
		if(a1_p > 0):
			real_rt= -(nav-a1_p)*100/a1_p
			real_rt=round(real_rt,3)
		
		
		if (real_rt < -0.45):
			print(subdict['fund_id'], subdict['fund_nm'], subdict['price'], '*',this.a1_p,real_rt,'%', subdict['fund_nav'], subdict['estimate_value'], subdict['discount_rt']) #subdict['apply_fee'], subdict['redeem_fee']
		
#print("once more")
myreq = Request('http://www.jisilu.cn/data/lof/index_lof_list/?___t=1459354520266')
myreq.add_header("Accept-Language", "en-US,en;q=0.5")
myreq.add_header("Connection", "keep-alive")	
myreq.add_header('Referer', "http://www.jisilu.cn/")
myreq.add_header("User-Agent", 'Mozilla/5.0 (Windows NT 6.1; rv:37.0) Gecko/20100101 Firefox/37.0')
lines = urlopen(myreq, timeout = 10).read()
js = json.loads(lines.decode('utf-8'))
lof_list=js['rows']
i=0
for i in range(len(lof_list)):
	mydicts=lof_list[i]
	subdict=mydicts['cell']
	discount_rt = float(subdict['discount_rt'][:-1])
	
	if(discount_rt < con_redeem):
		df = ts.get_realtime_quotes(subdict['fund_id'])
		this = df.loc[0]
		a1_p = float(this.a1_p)
		nav = float(subdict['fund_nav'])
		real_rt = 0
		if(a1_p > 0):
			real_rt= -(nav-a1_p)*100/a1_p
			real_rt=round(real_rt,3)
			
		if(real_rt<-0.45):
			print(subdict['fund_id'], subdict['fund_nm'], subdict['price'], '*',this.a1_p,real_rt,'%', subdict['fund_nav'], subdict['estimate_value'], subdict['discount_rt']) #subdict['apply_fee'], subdict['redeem_fee']
		

 
 
 
 #subdict['apply_fee'], subdict['redeem_fee']
				
		
		
#POST /data/lof/stock_lof_list/?___t=1459332174309 HTTP/1.1

#POST /jisiludata/etf.php?___t=1459332277981 HTTP/1.1

#POST /data/lof/stock_lof_list/?___t=1459332382795 HTTP/1.1


#POST /data/lof/index_lof_list/?___t=1459354520266 HTTP/1.1
