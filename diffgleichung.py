# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 14:50:28 2012

@author: casibus
"""
from numpy import *

import time

dt = 5 # "sekunden"
n0 = 1000

lambda_ = - 0.1
startzeit = 0
endzeit = int(100/dt)

n = zeros(endzeit)
n[0] = n0
dn = 0
# begin time measurement
tic = time.clock()

for t in range(startzeit,endzeit-1):
    dn = lambda_ * dt * n[t]
    n[t+1] = n[t] + dn
    #print 'Zeitpunkt t: n(t) = ',n[t]

# stop time measurement
toc = time.clock()
print toc - tic

# Plot the whole thing...
x_ = arange(startzeit,endzeit)*dt
from pylab import *
plot(x_,n)
x = arange(startzeit,endzeit*dt)
plot(n0*exp(lambda_*x))
# todo x-achse skalieren mit 1/dt
show()

