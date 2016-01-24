# -*- coding:utf-8 -*- 
#Created on 2015/3/14
#@author: Jimmy Liu

import json
#import re
#try:
from urllib.request import urlopen, Request
#except ImportError:
#    from urllib2 import urlopen, Request


#ts.get_loan_rate()
def jisilu_xsgbond():
	myreq = Request('http://www.jisilu.cn/data/cbnew/cb_list/, Query:___t=1453526981335')
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
	myreq = Request('http://www.jisilu.cn/data/stock/dividend_rate_list/, Query:___t=1453601688259')
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

			
jisilu_xsgbond()
jisilu_stockdiv()


	