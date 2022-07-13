#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 15:31:47 2022

@author: mustafauludag
"""
import numpy as np
import pandas as pd

# Series
myDict = {"Aslan": 10, "Polat": 20, "Pala": 30}
mySer = pd.Series(myDict)
print(mySer)  
names = ["Aslan", "Polat", "Pala","Memati"]
ages = [10, 20, 30, 40]
ageSeries = pd.Series(data=ages, index=names)
print(f"\n{ageSeries}")

# Dataframes

data = np.random.randn(4,3)
print(data)
dataFrame = pd.DataFrame(data)
print(dataFrame)

newDataFrame = pd.DataFrame(data,index=names,
  columns=["income","age", "working hours"])

print(newDataFrame)
print(newDataFrame["age"])
print(newDataFrame.loc["Aslan"])

## Change Index
newIndexList = ["bab","bob","dot","mot"]
newDataFrame["new Index"] = newIndexList
newDataFrame.set_index("new Index",inplace=True)



