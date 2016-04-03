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

#define the compare parameters
lof='160806'
index='sh000906'
start='2016-03-10'
end='2016-04-02'

lof = input("LOF: ")
index=input("Index: ")

	
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
	

code=lof
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
index_df=ts.get_hist_data(index,start,end)

newarray= DataFrame()

newarray[lof] = lof_df['p_change']
newarray[index] = index_df['p_change'] 
#newarray['gap'] = lof_df['p_change'] - index_df['p_change']
newarray['est_inc'] = newmoney['nav_inc_rt']
newarray['gap'] = lof_df['p_change'] - index_df['p_change']
newarray['est_nav'] = newmoney['nav']
print(newarray)
			
		


