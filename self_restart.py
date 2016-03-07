#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
####################################################################
# python 自动重启本程序
####################################################################
#import os,time
#def close():
#  print "程序重启！！！！"
#  print time.strftime('%Y.%m.%d-%H.%M.%S')
#  time.sleep(2) #3秒
#  p = os.popen('11111111.bat')
#  while True:
#    line = p.readline();
#    if '' == line:
#      break
#    print line
#if __name__ == '__main__':
#  close()
####################################################################
import time
import sys
import os
def restart_program():
  python = sys.executable
  os.execl(python, python, * sys.argv)

print('start...')
#  answer = raw_input("Do you want to restart this program ? ")
#  if answer.strip() in "y Y yes Yes YES".split():
#    restart_program()
print("3秒后,程序将结束...")
time.sleep(3)
restart_program()