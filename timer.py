#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

from threading import Timer
import time
import sys
import datetime

counter = 0

timer_interval = 1
canstart = 1

def delayrun():
	
	# Get a datetime object
	now = datetime.datetime.now()
	
	#print("Hour: %d" % now.hour)
	#print("Minute: %d" % now.minute)
	#print("Second: %d" % now.second)
	#print("Microsecond: %d" % now.microsecond)
    
	#method to restart to send notify email
	print('running+', now.hour,now.minute)
	
	if((now.hour == 18) and (now.minute==10)):
		print('prepare zero time')
	else:
		print('start run')
		
	
	print('running-')
	global canstart
	global counter 
	counter=counter+1
	print(counter)
	if(counter==3):
		x=0;
		try:
			j=100/x
		except:
			print('let it go')
	canstart = 1

	#print('change canstart', canstart)
	


while True:
	t = Timer(timer_interval,delayrun)
	time.sleep(0.1)
	#print('canstart', canstart)
	
	
	
	if(canstart==1):
		t.start()
		canstart = 0
	#if counter > 10:
		#print('will exit')
		#sys.exit()

	#print('main running')