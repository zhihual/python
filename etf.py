#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

import tushare as ts

#ts.sh_margins('2015-01-03', '2015-04-07')

#ts.shibor_data()

#df = ts.get_realtime_quotes(['sh','sz','cyb','510300','159915','000725','150200','511880','204001','131810'])


#df = ts.get_realtime_quotes(['510300','159915','000725','150200','511880','511990','204001','131810'])

df = ts.get_realtime_quotes(['204001'])

mydf = df['code']
df = df.drop(['name','open', 'pre_close', 'bid', 'ask', 'amount','a2_p', 'a3_v','a3_p', 'a4_v', 'a5_v', 'a5_p','date', 'code',
               'b1_v', 'b2_p', 'b2_v', 'b2_p', 'b3_v', 'b4_v', 'b4_p','b5_v', 'b5_p', 'a1_v', 'a2_v', 'a4_p', 'b1_p', 'b3_p', 'a1_p'], axis=1)



df.insert(0,'code', mydf[:])

Invest = 130*10000

#print(mydf)               
print(df)
gc001 = df.price
gc001=float(gc001[0])
print(gc001)
gc001=1.8
Ret = (Invest*gc001/100/360)-(Invest*0.001/100)
Ret = round(Ret, 2)
print(Ret)

#185.65

#110.9

CashRet = 110.9

CashRate = CashRet*365/Invest*100
CashRate = round(CashRate,2)
print(CashRate,'%')


df = ts.get_realtime_quotes(['511880'])

mydf = df['code']
df = df.drop(['name','open', 'pre_close', 'bid', 'ask', 'amount','a2_p', 'a3_v','a3_p', 'a4_v', 'a5_v', 'a5_p','date', 'code',
               'b1_v', 'b2_p', 'b2_v', 'b2_p', 'b3_v', 'b4_v', 'b4_p','b5_v', 'b5_p', 'a1_v', 'a2_v', 'a4_p', 'b1_p', 'b3_p', 'a1_p'], axis=1)

df.insert(0,'code', mydf[:])

yinhua_buy=100.555

yinhua_cur = df.price
yinhua_cur = float(yinhua_cur[0])
print(yinhua_cur)

share = 1300*10000

yinhuaret=share/100*(yinhua_cur-yinhua_buy)

print(yinhuaret)






