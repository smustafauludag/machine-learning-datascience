#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 10:28:21 2022
    
@author: mustafauludag
"""
import numpy as np

arr1 = np.arange(0,11,2)
print(f"arange=> {arr1}")
arr2 = np.linspace(0, 10,6)
print(f"linspace=> {arr2}")

identityMatrix = np.eye(3)
I=np.identity(3) 
print(identityMatrix)
print(I)

#argmax index of max value
#argmin index of min value