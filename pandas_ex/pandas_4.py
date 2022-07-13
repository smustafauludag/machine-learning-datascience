#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 10:41:09 2022

@author: mustafauludag
"""

import pandas as pd
import numpy as np

# =============================================================================
# Grouping
# =============================================================================

salaryData = {"Department":["Software","Software","Hardware","Hardware","Marketing","Marketing"],
              "Name":   ["Ahmet","Mehmet","Atil","Burak","Zeynep","Fatma"],
              "Salary": [100,150,200,300,400,500]}

salaryDataFrame = pd.DataFrame(salaryData)
print(salaryDataFrame)
salaryGroupDep = salaryDataFrame.groupby("Department")

print(salaryGroupDep.count())
print(salaryGroupDep.mean()) #min, max
print(salaryGroupDep.describe())

# =============================================================================
# Concat
# =============================================================================

momData1 = {"Name": ["mom1","mom2","mom3"],
           "Age": [33,35,28]}

momData2 = {"Name": ["mom4","mom5","mom6"],
           "Age": [36,55,43]}

momDataFrame1 = pd.DataFrame(momData1)
momDataFrame2 = pd.DataFrame(momData2)
concatMomDataFrame = pd.concat([momDataFrame1,momDataFrame2],axis=0)

print(momDataFrame1)
print(momDataFrame2)
print(concatMomDataFrame)
print("\n")


# =============================================================================
# Merge
# =============================================================================

momAge = {"Name": ["mom1","mom2","mom3"],
          "Age": [33,35,28]}

momWeight = {"Name": ["mom1","mom2","mom3"],
             "Weight": [68,70,80]}

ageDataFrame = pd.DataFrame(momAge)
weightDataFrame = pd.DataFrame(momWeight)
mergedDataFrame = pd.merge(ageDataFrame, weightDataFrame)


print(ageDataFrame)
print(weightDataFrame)
print(mergedDataFrame)

# =============================================================================
# Apply
# =============================================================================

def power_of_3(x): return x**3
new_dataframe = mergedDataFrame["Age"].apply(power_of_3)
print(new_dataframe)

