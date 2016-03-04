#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

from threading import Timer
import time

timer_interval = 1
canstart = 1

def delayrun():
	print('running')
	global canstart
	canstart = 1
	#print('change canstart', canstart)
	


while True:
	t = Timer(timer_interval,delayrun)
	time.sleep(0.1)
	#print('canstart', canstart)
	if(canstart==1):
		t.start()
		canstart = 0
		
	#print('main running')