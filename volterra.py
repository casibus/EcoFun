# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 16:07:07 2012

@author: casibus
"""

from numpy import *

import time

# Parameter:
dt = 0.1 # "tage"
n0_hunter = 30
n0_prey = 100
a = birthrate_prey = 0.1 # 0.1 jungtiere pro tag
b = 0.005#eating_rate = 0.01
# birthrate_hunter = 0.01
# natural_death_rate_prey = 0.5 * birthrate_prey

g = natural_death_rate_hunter = -0.35 #0.5 * birthrate_hunter
d = 0.004#bio_mass_addition_rate_for_hunter_per_prey = 0.000000001

startzeit = 0
endzeit = int(2000/dt)

h = zeros(endzeit)
p = zeros(endzeit)

h[0] = n0_hunter 
p[0] = n0_prey
n = 0.0001
for t in range(startzeit,endzeit-1):
    dp = (a*p[t] - b*p[t]*h[t] - n*p[t]**2)*dt
    dh = (g*h[t] + d*p[t]*h[t])*dt
    h[t+1] = h[t]+dh
    
    p[t+1] = p[t]+ dp
    if h[t+1] < 0:
        h[t+1] = 0
    if p[t+1] < 0:
        p[t+1] = 0
    
print h
print p
    
from pylab import *
plot(h, color ='red')
plot(p, color ='blue')
show()