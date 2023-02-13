#!/bin/env python3

# John Haggerty, BNL
# 2021.02.17

from lvcontrol import *
import time

tn = lv_connect('10.20.34.122')
for i in range(2):
	lv_enable(tn,i+1,1)
	time.sleep(1)
lv_disconnect(tn)    