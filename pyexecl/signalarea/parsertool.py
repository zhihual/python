#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from openpyxl import load_workbook
from openpyxl import Workbook
from openpyxl import worksheet
import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

#  1. ��ʲô?  ���������λ����Ϣ������λ�ö�Ӧ������ 
#  2. ��ʲô�ô���  ������ʾ���л����µ��ź����Ʒֲ����ҵ��źŻ�۵㡣���ȵ㡣
#                   ����python�����̶�
#  3. ��ô����
#            a. ��ȡ������� �ֹ����� execl��� �����Ҫ�أ� ��źͻ�ַ. ������Ա�����ѯ
#            b. ����������ͼ�ϣ�ת��mac��ַΪ��Ÿ�ʽ��ͬ������� ��ѯexcel�� ͬ���������ַ
#
#
#
#


def openWhiteList(excelName):  #excelname �������excel���,��������handle
    print(excelName)
    wb = load_workbook(excelName)
    #ws = wb.active
    #print(len(tuple(ws.rows)), len(tuple(ws.columns)))
    return wb


def queryMeterAddr(excelhdl, meterId):#���ݵ��id,�ڵ��Ӱ������в�ѯ��ַ
    row_num = len(tuple(excelhdl.rows))
    columns_num = len(tuple(excelhdl.columns))
    #print(row_num, columns_num)
    for idx in range(1,row_num):
        #print(excelhdl['A'+str(idx)].value, excelhdl['B'+str(idx)].value)
        val = str(excelhdl['A'+str(idx)].value)
        val = val.strip()
        if val == meterId:
            val = str(excelhdl['B'+str(idx)].value)
            return val
    return ''

#def queryMeterId(excelhdl, meterAddr):
#    print('hello')
    

def convertMacToMeterId(mac):#��mac��ַת��Ϊ��id, return meterId
    mac = mac.strip()
    mac = mac.lstrip('\t')
    mac = mac.rstrip('\r\n')
    mac = mac.replace(':', '')
    #print(mac)
    val = mac[10:12]+mac[8:10]+mac[6:8]+mac[4:6]+mac[2:4]+mac[0:2]
    #print(val)
    return val
    

#def convertMeterIdToMac(meterId):#Convert meterId to Mac style. return Mac   


def openTopoTxt(topoTxtName):#topo txt file name, return handle
    print(topoTxtName)
    f = fopen(topoTxtName)
    return f


def putInfobyMac(topohdl, infoStr, placeMark):#output infoStr to topo table
    print('hello')

#begin of main function

#main()

whitelListName='whitelist.xlsx'

whiteList = Workbook() 

topoTxtName='topo.txt'

whiteList= openWhiteList(whitelListName)

whiteListSheet = whiteList.active




#Test Code Code
#Test open excel
print(len(tuple(whiteListSheet.rows)), len(tuple(whiteListSheet.columns)))



#Test MeterId
tMeterId = '110120061848'

tMeterAddr = queryMeterAddr(whiteListSheet, tMeterId)
print(tMeterId, tMeterAddr.decode('gbk'))

#Test Convert Meter Mac
tMeterMac = '18:77:06:20:01:11'

tConverMeterId = convertMacToMeterId(tMeterMac)
print(tMeterMac)
print(tConverMeterId)

#Test open txt
_list_content = []

fh=open(topoTxtName, 'rb')

for i in fh.readlines():
    _list_content.append(i)
fh.close()

_content = ''
for i in _list_content:
    if(i.find(':') >= 0):
        meter_id = convertMacToMeterId(i)
        addr = queryMeterAddr(whiteListSheet, meter_id)
        _content += i[:-3] +'    '+ addr +'\r\n'

open('result.txt', 'wb').writelines(_content)        











