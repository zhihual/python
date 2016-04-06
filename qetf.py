#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

import json
#import re
try:
	from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

import tushare as ts
from pandas import Series, DataFrame	
import datetime	

#con_redeem = 10


con_disc=input("con_disc: ")

if(con_disc == ''):
	con_disc = -0.7
	print('default con_disc:%f', con_disc)
else:
	con_disc=float(con_disc)

con_redeem = con_disc

current = datetime.datetime.now()

end ='%s-%s-%s' %(current.year,current.month, current.day)
	
start='2016-03-10'
#end='2016-04-02'
#end='2016-04-05'

def FormNavHistTable(str):
	ser_data={'nav':[],'nav_inc_rt':[]}
	ser_inx=[]
	index = 0
	match1='<td>201'
	match2='tor bold'
	match3='tor bold'

	while(str.find(match1) > 0):
		loc_match1=str.find(match1)
		loc_match1 = loc_match1+4
		tempstr=str[loc_match1:]
		loc_match2=tempstr.find(match2)
		loc_match2+=10
		data = str[loc_match1:loc_match1+10]
		nav = tempstr[loc_match2:loc_match2+6]
		tempstr = tempstr[loc_match2+7:]
		loc_match3 = tempstr.find(match3)
		tempstr=tempstr[loc_match3+8:]
		loc_match3 = tempstr.find(match3)
		loc_match3+=14
		if(tempstr[loc_match3] == '-'):
			inc_rt = tempstr[loc_match3:loc_match3+6]
		else:
			inc_rt = tempstr[loc_match3:loc_match3+5]
		#print(data,nav,inc_rt)
		ser_inx.insert(index,data)
		ser_data['nav'].insert(index,nav)
		ser_data['nav_inc_rt'].insert(index,inc_rt)
		str = tempstr[loc_match3+6:]
		index+=1
	#print(ser_data)
	myarry= DataFrame(ser_data, columns=['nav','nav_inc_rt'], index=ser_inx)
	#print(myarry)
	return myarry
	
def QNav(lof, index, start, end):
	code=lof

	if(lof =='161033'):
		return
	
	url = 'http://fund.eastmoney.com/f10/F10DataApi.aspx?type=lsjz&code=%s&page=1&per=20&sdate=&edate=&rt=0.36159112700261176'%(code)

	myreq = Request(url)
	myreq.add_header("Accept-Language", "en-US,en;q=0.5")
	myreq.add_header("Connection", "keep-alive")	
	myreq.add_header('Referer', "http://fund.eastmoney.com")
	myreq.add_header("User-Agent", 'Mozilla/5.0 (Windows NT 6.1; rv:37.0) Gecko/20100101 Firefox/37.0')
	lines = urlopen(myreq, timeout = 10).read()
	lines = lines.decode('GBK')
	newmoney = FormNavHistTable(lines)

	lof_df = ts.get_hist_data(lof,start,end)
	
	if(index == '000906'):
		index = 'sh000906'
	index_df=ts.get_hist_data(index,start,end)
	newarray= DataFrame()

	newarray[lof] = lof_df['p_change']
	newarray[index] = index_df['p_change'] 
	#newarray['gap'] = lof_df['p_change'] - index_df['p_change']
	newarray['est_inc'] = newmoney['nav_inc_rt']
	newarray['gap'] = lof_df['p_change'] - index_df['p_change']
	newarray['est_nav'] = newmoney['nav']
	print(newarray)		






myreq = Request('http://www.jisilu.cn/data/lof/stock_lof_list/?___t=1459332174309')
myreq.add_header("Accept-Language", "en-US,en;q=0.5")
myreq.add_header("Connection", "keep-alive")	
myreq.add_header('Referer', "http://www.jisilu.cn/")
myreq.add_header("User-Agent", 'Mozilla/5.0 (Windows NT 6.1; rv:37.0) Gecko/20100101 Firefox/37.0')
lines = urlopen(myreq, timeout = 10).read()
js = json.loads(lines.decode('utf-8'))
lof_list=js['rows']
i=0

print('fund_id fund_nm fund_nav a1_p real_rt stock_ratio all_amount stock_increase_rt') 
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
		
		
		if (real_rt < con_disc):
			print(subdict['fund_id'], subdict['fund_nm'],   subdict['fund_nav'],'*',this.a1_p,real_rt,'%', subdict['stock_ratio'], subdict['all_amount'], subdict['stock_increase_rt'],discount_rt) 
			
			
		
print("index level=%.1f" % con_disc)

print('fund_id fund_nm fund_nav a1_p real_rt index_id index_nm index_increase_rt') 

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
			
		if(real_rt<con_disc):
			print(subdict['fund_id'], subdict['fund_nm'],   subdict['fund_nav'],'*',this.a1_p,real_rt,'%', subdict['index_id'],subdict['index_nm'],subdict['index_increase_rt'],discount_rt)
            		
			QNav(subdict['fund_id'], subdict['index_id'], start,end)
			





	

	


 
 

				
		
		
#POST /data/lof/stock_lof_list/?___t=1459332174309 HTTP/1.1

#POST /jisiludata/etf.php?___t=1459332277981 HTTP/1.1

#POST /data/lof/stock_lof_list/?___t=1459332382795 HTTP/1.1


#POST /data/lof/index_lof_list/?___t=1459354520266 HTTP/1.1
