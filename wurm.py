# -*- coding: utf-8 -*-
"""
Created on Fri Jun 01 14:28:20 2012

@author: casibus
"""

# This program shell simulate a 
# worm that travels along a temperature 
# gradient by a random walk to a "food source"

# What do we need?
# ===> A worm and an temperature landscape,
# Movement

from numpy import *

landscape = zeros((100,100),) 
zeros(