#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

import datetime
# Get a datetime object
now = datetime.datetime.now()
# General functions 
print("Year: %d" % now.year)
print("Month: %d" % now.month)
print("Day: %d" % now.day)
print("Weekday: %d" % now.weekday())
# Day of week Monday = 0, Sunday = 6
print("Hour: %d" % now.hour)
print("Minute: %d" % now.minute)
print("Second: %d" % now.second)
print("Microsecond: %d" % now.microsecond)
# ISO Functions
print("ISO Weekday: %d" % now.isoweekday())
# Day of week Monday = 1, Sunday = 7
print("ISO Format: %s" % now.isoformat())
# ISO format, e.g. 2010-12-24T07:10:52.458593
print("ISO Calendar: %s" % str(now.isocalendar()))
# Tuple of (ISO year, ISO week number, ISO weekday)
# Formatted date
print(now.strftime("%Y/%m/%d"))