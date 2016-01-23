# -*- coding:utf-8 -*- 
#Created on 2015/3/14
#@author: Jimmy Liu

import json
#import tushare as ts
#import pandas as pd
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request


#ts.get_loan_rate()
	
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
	#if (len(subdict['redeem_tc'])>0):
	print('    ',subdict['redeem_tc'])
	#if (len(subdict['put_tc'])>0):
	print('    ',subdict['put_tc'])
	print()
#df = pd.DataFrame.from_dict(subdict,orient='index')

#print(subdict)
#print(len(subdict))
#print(df)



	