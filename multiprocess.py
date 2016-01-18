#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import os

print('Process (%s) start...' % os.getpid())

pid = os.fork()

if pid == 0:
	print('child process(%s), my parent is %s' %(os.getpid(), os.getppid()))
else:
	print('I(%s) create one child(%s)' %(os.getpid(), pid))
