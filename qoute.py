#!/usr/bin/env python3
# -*- coding:utf-8 -*- 


import tushare as ts


quotelist = ['510050','510300','159915','204001','131810','511880','511990','000725','150200','000656','002739']

df = ts.get_realtime_quotes(quotelist)
mydf = df['code']
df = df.drop(['pre_close','open','bid', 'ask', 'amount','a2_p', 'a3_v','a3_p', 'a4_v', 'a5_v', 'a5_p','date', 'code',
              'b1_v', 'b2_p', 'b2_v', 'b2_p', 'b3_v', 'b4_v', 'b4_p','b5_v', 'b5_p', 'a1_v', 'a2_v', 'a4_p', 'b1_p', 'b3_p', 'a1_p','volume'], axis=1)
    
	
df.insert(0,'code', mydf[:])
mydispy = df.drop(['name'],axis=1)
print(mydispy)