#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

import json
#import re
try:
	from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

cons_redeem = -1.0
cons_sell = 3.5	
	
#myreq = Request('http://www.jisilu.cn/data/sfnew/funda_list/?___t=1459333211443') #pure a
myreq = Request('http://www.jisilu.cn/data/sfnew/arbitrage_vip_list/?___t=1459335497584')
myreq.add_header("Accept-Language", "zn-CN,zh;q=0.8")
myreq.add_header("Connection", "keep-alive")	
myreq.add_header('Referer', "http://www.jisilu.cn/sfnew")
myreq.add_header("User-Agent", 'Mozilla/5.0 (Windows NT 6.1; rv:37.0) Gecko/20100101 Firefox/37.0')
#Key step to sovle problem
myreq.add_header("Cookie", 'kbz__user_login=1ubd08_P1ebax9aX28vhxtvtwpGcoenW3Ozj5tTav9CjlKjFpNynzK-e3Zncx6zew9XHqbHboK7Q3MSnk9eukaeCr6bq0t3K1I2pk6yxlZGcoc62x9aXxNHwyt_kwp-WoqmVkdDV5cbl2OaYr8SBqqempJnDxrmslZyYouDR4N7Mztu34Nallqavj6OXlKHAsc25w46WzdzjxpCo2dzg2KKMusro0ODdkKSXoqmjm62lp5Cul5PLwtbC5uKknqyjpZWs; kbz_newcookie=1; kbzw_r_uname=dikehua; kbzw__user_login=7Obd08_P1ebax9aX28vhxt_s1JmcndHV7Ojg6N7bwNOMqq_XqMSixKqr26Df0rDI2MbdrKvemKXF2dumm92ip5mXnKTs3Ny_zYynq66irY2yj8ui1dSexdDqyuDl1piumqeCnrjg5dfn2OOBws2Vn6edsoLNsM6tp6GBsdHk5drA3s7Cy-qQrKqqppSmgZzEvb3GuKOC4sri3JO_xtPM46KVrOHe5s_bkKutoaiPopWtqaOhr4zKw9zC6eCirZSnj6ev; kbzw__Session=u11l96t1m1acgv8np5jlbec0p4; Hm_lvt_164fe01b1433a19b507595a43bf58262=1459141116,1459219997,1459230467,1459233839; Hm_lpvt_164fe01b1433a19b507595a43bf58262=1459391748')
#key step
lines = urlopen(myreq, timeout = 10).read()
js = json.loads(lines.decode('utf-8'))
lof_list=js['rows']
i=0
for i in range(len(lof_list)):
	mydicts=lof_list[i]
	subdict=mydicts['cell']
	apply_sell = float(subdict['apply_sell'])
	apply_sell = round(apply_sell, 2)
	buy_redeem = float(subdict['buy_redeem'])
	buy_redeem = round(buy_redeem, 2)
	
	sell1A = float(subdict['sell1A'])
	sell1B = float(subdict['sell1B'])
	
	buy1A = float(subdict['buy1A'])
	buy1B = float(subdict['buy1B'])
	
	
	base_nav = float(subdict['base_nav'])
	base_est_val = float(subdict['base_est_val'])
	
	
	redeem_price = (sell1A+sell1B)/2
	redeem_price = round(redeem_price,3)
	self_count = (base_nav - redeem_price)*100/redeem_price
	self_count = round(self_count,3)
	
	est_count = (base_est_val-redeem_price)*100/redeem_price
	est_count = round(est_count,3)
	
	sell_price = (buy1A+buy1B)/2
	sell_price = round(sell_price,3)
	
	#print(i)
	if((buy_redeem < cons_redeem)):
		#print("apply_sell = %f" % apply_sell)
		print( subdict['fundA_id'],subdict['fundB_id'], subdict['base_fund_id'], subdict['base_fund_nm'], subdict['buy_redeem'],'%', subdict['fundA_volume'], subdict['fundB_volume']) 
		print(subdict['base_nav'],subdict['sell1A'], subdict['sell1B'], redeem_price,self_count,'%', '(',subdict['base_est_val'], est_count,'%',')')
	if(apply_sell>cons_sell):
		print( subdict['fundA_id'],subdict['fundB_id'], subdict['base_fund_id'], subdict['base_fund_nm'], subdict['apply_sell'],'%', subdict['fundA_volume'], subdict['fundB_volume']) 
		print(subdict['base_nav'],subdict['buy1A'], subdict['buy1B'],sell_price)
	










	
# fundA_id":"150036"
#"fundA_nm":"\u5efa\u4fe1\u7a33\u5065"
#"fundB_id":"150037"
#"fundB_nm":"\u5efa\u4fe1\u8fdb\u53d6",
#"base_fund_id":"165310",
#"base_fund_nm":"\u5efa\u4fe1\u53cc\u5229",
#"index_id":"399300",
#"index_nm":"\u4e3b\u52a8\u57fa\u91d1",
#"status_cd":"N",
#"recalc_to":null,"calc_info":null,
#"fund_company_nm":"\u5efa\u4fe1\u57fa\u91d1",
#"coupon_next":"5.000",
#"a_ratio":4,
#"b_ratio":6,
#"asset_ratio":"80%",
#"maturity_dt":"-",
#"apply_fee":"1.5%",
#"apply_fee_tip":"100\u4e07\u4ee5\u4e0b\uff0c1.5%\r\n100\u4e07(\u542b)\u81f3500\u4e07\uff0c1%\r\n500\u4e07(\u542b)\u4ee5\u4e0a\uff0c\u6bcf\u7b141000\u5143",
#"redeem_fee":"0.5%",
#"redeem_fee_tip":"0.5%",
#"notes":"http:\/\/www.ccbfund.cn\/fund_info\/info.jspx?fundCode=165310",
#"base_nav":"1.2110",
#"base_nav_dt":"2016-03-29",
#"b_gangan":"1.487",
#"base_lower_recalc_rt":"57.54%",
#"base_est_val":"1.2360",
#"a_profit_rt_next":"4.721",
#"base_est_dis_rt":"3.50%",
#"idx_incr_rt":"2.58%",
#"real_idx_increase_rt":"2.58",
#"b_est_val":"1.385",
#"est_time":"2016-03-30 15:10:05",
#"lower_recalc_rt":"57.54",
#"buy_redeem":"3.80",
#"apply_sell":"-0.73",
#"priceA":"1.071",
#"sell1A":"1.085",
#"buy1A":"1.071",
#"sell1_amountA":"2.470",
#"buy1_amountA":"0.434",
#"fundA_nav":"1.0120",
#"fundA_nav_dt":"2016-03-29",
#"fundA_volume":"3.64",
#"fundA_last_dt":"2016-03-30",
#"fundA_last_time":"14:58:05",
#"fundA_stock_volume":"3.3764",
#"increase_rtA":"-0.74%",
#"priceB":"1.418",
#"sell1B":"1.415",
#"buy1B":"1.331",
#"sell1_amountB":"0.800",
#"buy1_amountB":"0.700",
#"fundB_nav":"1.3440",
#"fundB_nav_dt":"2016-03-29",
#"fundB_volume":"14.89",
#"fundB_last_dt":"2016-03-30",
#"fundB_last_time":"14:56:27",
#"fundB_stock_volume":"10.9412",
#"increase_rtB":"4.65%",
#"asset_ratio_num":"80.00",
#"asset_ratio_last":"120%",
#"ownedA":0,
#"ownedM":0,
#"is_est_val":1,
#"is_last_nav":1,
#"funda_name_tip":"\u4e0b\u671f\u5229\u7387\uff1a5.00\uff0c\u4fee\u6b63\u6536\u76ca\u7387\uff1a4.72%",
#"abrate":"4:6",
#"coupon":"0.00%",
#"merge_price":"1.2792",
#"AB_price":"\u73b0\u4ef7A\/B : 1.071\/1.418",
#"est_dis_rt":"3.50%","min_apply_amount":null,
#"fundA_amount":"197","fundA_amount_increase_rt":"0.00%",
#"fundA_amount_increase":"0","fundB_amount_increase":"0",
#"fundA_turnover_rt":"1.71%",
#"fundA_amount_tip":"2016-03-30 A\u7c7b\u603b\u4efd\u989d197.000\u4e07\u4efd\uff0c\u4efd\u989d\u589e\u957f0.00%",
#"fundA_stock_volume_tip":"A\u7c7b\u603b\u4efd\u989d197.000\u4e07\u4efd, \u6210\u4ea43\u4e07\u4efd",
#"fundB_amount":295.5,"fundB_turnover_rt":"3.70%","fundB_amount_tip":"2016-03-30 B\u7c7b\u603b\u4efd\u989d296\u4e07\u4efd\uff0c\u4efd\u989d\u589e\u957f0.00%",
#"fundB_stock_volume_tip":"B\u7c7b\u603b\u4efd\u989d296\u4e07\u4efd, \u6210\u4ea411\u4e07\u4efd"
#POST /data/sfnew/arbitrage_vip_list/?___t=1459333493746 HTTP/1.1

