#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 09:23:53 2022

@author: mustafauludag
"""
import numpy as np
import pandas as pd

# Multi Index

firstIndex = ["Simpson","Simpson","Simpson",
              "South Park","South Park","South Park"]

innerIndex = ["Homer","Bart","Marge",
              "Cartman", "Kenny","Kyle"]

addedİndex = list(zip(firstIndex,innerIndex))
print(addedİndex)

addedIndex = pd.MultiIndex.from_tuples(addedİndex)
print(addedİndex)

data = np.array([[40,"A"],
                 [10,"B"],
                 [30,"C"],
                 [9,"D"],
                 [10,"E"],
                 [11,"E"]])
dataFrame = pd.DataFrame(data=data,
                         index=addedIndex,
                         columns=["age","job"])
dataFrame.index.names = ["Movie", "Name"]
print(dataFrame)

