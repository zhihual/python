#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

import json
#import re
try:
	from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request


def RemoveHTML(str):
	match1='">'
	match2='span>'
	loc_match1=str.find(match1)
	if(loc_match1 < 0):
		return str
	loc_match1+=2
	loc_match2=str.find(match2)
	loc_match2-=2
	
	
	return str[loc_match1:loc_match2]+'*'
	
#ts.get_loan_rate()
def jisilu_xsgbond():
	#myreq = Request('http://www.jisilu.cn/data/cbnew/cb_list/, Query:___t=1453526981335')
	myreq = Request('http://www.jisilu.cn/data/cbnew/cb_list/?___t=1453714142180')
	myreq.add_header("Accept-Language", "en-US,en;q=0.5")
	myreq.add_header("Connection", "keep-alive")
	myreq.add_header('Referer', "http://www.jisilu.cn/")
	myreq.add_header("User-Agent", 'Mozilla/5.0 (Windows NT 6.1; rv:37.0) Gecko/20100101 Firefox/37.0')
	lines = urlopen(myreq, timeout = 10).read()

	js = json.loads(lines.decode('utf-8'))
	#lines to json, json->list, list->dict
	bond_list=js['rows']
	i=0
	for i in range(len(bond_list)):
		mydicts=bond_list[i]
		subdict=mydicts['cell']
		print(subdict['bond_id'], subdict['bond_nm'], subdict['price']) 
		#print('    ',subdict['redeem_tc'])
		#print('    ',subdict['put_tc'])
		#print()
		#df = pd.DataFrame.from_dict(subdict,orient='index')

def jisilu_stockdiv():
	#myreq = Request('http://www.jisilu.cn/data/stock/dividend_rate_list/, Query:___t=1453601688259')
	myreq = Request('http://www.jisilu.cn/data/stock/dividend_rate_list/?___t=1453714401268')
	myreq.add_header("Accept-Language", "en-US,en;q=0.5")
	myreq.add_header("Connection", "keep-alive")
	myreq.add_header('Referer', "http://www.jisilu.cn/")
	myreq.add_header("User-Agent", 'Mozilla/5.0 (Windows NT 6.1; rv:37.0) Gecko/20100101 Firefox/37.0')
	lines = urlopen(myreq, timeout = 10).read()

	js = json.loads(lines.decode('utf-8'))
	divstock_list=js['rows']
	i=0
	for i in range(len(divstock_list)):
		mydicts=divstock_list[i]
		subdict=mydicts['cell']
	
		rate = subdict['dividend_rate']
		rate = rate[:-1] 
		#print(rate)
		if float(rate) > 6.0:
			print(subdict['stock_id'], subdict['stock_nm'], subdict['price'], subdict['dividend_rate'], subdict['pe'], subdict['pb']) 		

def jisilu_newbond():
	myreq = Request('http://www.jisilu.cn/jisiludata/NewBond.php?Query:qtype=apply&___t=1453606568869&rp=22&page=1')
	myreq.add_header("Accept-Language", "en-US,en;q=0.5")
	myreq.add_header("Connection", "keep-alive")
	myreq.add_header('Referer', "http://www.jisilu.cn/")
	myreq.add_header("User-Agent", 'Mozilla/5.0 (Windows NT 6.1; rv:37.0) Gecko/20100101 Firefox/37.0')
	lines = urlopen(myreq, timeout = 10).read()
	js = json.loads(lines.decode('utf-8'))
	newbond_list=js['rows']
	i=0
	for i in range(len(newbond_list)):
		mydicts=newbond_list[i]
		subdict=mydicts['cell']
		rate = subdict['coupon']
		rate = rate[:-1] 
		if float(rate) > 4.0:
			print(subdict['bond_id'], subdict['bond_nm'], subdict['apply_dt'], subdict['apply_id'], subdict['coupon'],subdict['bond_rating_cd'], subdict['guarantor'])

def jisilu_newstock():
	myreq = Request('http://www.jisilu.cn/jisiludata/newstock.php?Query:qtype=apply&___t=1453623108306&rp=22&page=1&pageSize=50')
	myreq.add_header("Accept-Language", "en-US,en;q=0.5")
	myreq.add_header("Connection", "keep-alive")
	myreq.add_header('Referer', "http://www.jisilu.cn/")
	myreq.add_header("User-Agent", 'Mozilla/5.0 (Windows NT 6.1; rv:37.0) Gecko/20100101 Firefox/37.0')
	lines = urlopen(myreq, timeout = 10).read()
	js = json.loads(lines.decode('utf-8'))
	newstock_list=js['rows']
	i=0
	for i in range(len(newstock_list)):
		mydicts=newstock_list[i]
		subdict=mydicts['cell']
		#print('1',subdict['apply_dt'], subdict['apply_cd'])
		my_apply_dt = RemoveHTML(subdict['apply_dt'])
		my_apply_cd = RemoveHTML(subdict['apply_cd'])
		#print('2', my_apply_dt, my_apply_cd)
		print(subdict['stock_cd'], my_apply_dt, my_apply_cd, subdict['stock_nm'],)
		#print(subdict['apply_dt'])

def jisilu_etf():
	myreq = Request('http://www.jisilu.cn/jisiludata/etf.php?Query:___t=1453624119049')
	myreq.add_header("Accept-Language", "en-US,en;q=0.5")
	myreq.add_header("Connection", "keep-alive")	
	myreq.add_header('Referer', "http://www.jisilu.cn/")
	myreq.add_header("User-Agent", 'Mozilla/5.0 (Windows NT 6.1; rv:37.0) Gecko/20100101 Firefox/37.0')
	lines = urlopen(myreq, timeout = 10).read()
	js = json.loads(lines.decode('utf-8'))
	etf_list=js['rows']
	i=0
	for i in range(len(etf_list)):
		mydicts=etf_list[i]
		subdict=mydicts['cell']
		print(subdict['fund_id'], subdict['fund_nm'], subdict['price'],  subdict['increase_rt'],subdict['volume'], subdict['discount_rt'])
		
#jisilu_xsgbond()
#jisilu_stockdiv()
#jisilu_newbond()
jisilu_newstock()
#jisilu_etf()
	