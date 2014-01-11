#!/usr/bin/env python

import nxt.locator
from nxt.sensor import *

b = nxt.locator.find_one_brick()

print 'Light:', Light(b, PORT_2).get_sample()
print ' Color:',  Color20(b, PORT_3).get_sample()
print 'Ultrasonic:', Ultrasonic(b, PORT_4).get_sample()
