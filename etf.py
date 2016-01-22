#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

import tushare as ts

#ts.sh_margins('2015-01-03', '2015-04-07')

#ts.shibor_data()

df = ts.get_realtime_quotes(['sh','sz','cyb','510300','159915','000725','150200','131810','204001','510050'])

mydf = df['code']
df = df.drop(['name','open', 'pre_close', 'bid', 'ask', 'amount','a2_p', 'a3_v','a3_p', 'a4_v', 'a5_v', 'a5_p','date', 'code',
               'b1_v', 'b2_p', 'b2_v', 'b2_p', 'b3_v', 'b4_v', 'b4_p','b5_v', 'b5_p', 'a1_v', 'a2_v', 'a4_p', 'b1_p', 'b3_p', 'a1_p'], axis=1)



df.insert(0,'code', mydf[:])

#print(mydf)               
print(df)
