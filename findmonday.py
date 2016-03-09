#!/usr/bin/env python  
# _#_ coding:utf-8 _*_  
  
""" 
#获取一年中每个星期的起始时间 
#author:yqj@fccs.com 
#http://blog.csdn.net/youngqj/article/details/12905877
#opencv, 视觉
"""  
import datetime  
import time  
  
current = datetime.datetime.now()  
start = datetime.date(current.year,1,1)  
last_day = datetime.date(current.year,12,31)  
isfirst = start.weekday()  
last_week = last_day.strftime('%W')  
  
#print(start,last_day,isfirst,last_week)
  
weeks={}  
if isfirst !=0:  
    end = datetime.timedelta(7-start.weekday()-1)  
    weeks[0]=[start,start+end]  
start += datetime.timedelta(7 - start.weekday())  
#print(weeks[0],str(weeks[0][0]))
def print_date(i):  
    days = datetime.timedelta(weeks=i)
    #print(days)
    end = start + days #每周的开始时间  
    ##print('i',days,end)  
    if  i+1 == int(last_week):  
	    weeks[i+1] = [end,last_day]  
    else:  
	    weeks[i+1] = [end,end + datetime.timedelta(6)]  
  
def allweeks():  
    for i in range(0, int(last_week)):  
	    print_date(i)
    return weeks    
          
def main():  
  
    allweeks()  
  
    for (k,week) in weeks.items():  
        num = k+1<=9 and "0"+str(k+1) or str(k+1)  
        print("%s\t%s\t%s\t" %(str(current.year)+num,str(week[0]),str(week[1])))
  
if __name__ == "__main__":  
    main()  