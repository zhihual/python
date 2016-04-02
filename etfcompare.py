#!/usr/bin/env python3
# -*- coding:utf-8 -*- 


#!/usr/bin/env python3
# -*- coding:utf-8 -*- 


import tushare as ts
from pandas import Series, DataFrame

#define the compare parameters
lof='160806'
index='000906'
start='2016-03-10'
end='2016-04-02'

lof = input("LOF: ")
index=input("Index: ")


lof_df = ts.get_hist_data(lof,start,end)
index_df=ts.get_hist_data(index,start,end)

newarray= DataFrame()

newarray[lof] = lof_df['p_change']
newarray[index] = index_df['p_change'] 
newarray['gap'] = lof_df['p_change'] - index_df['p_change']
print(newarray)