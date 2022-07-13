#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 10:11:02 2022

@author: mustafauludag
"""

import numpy as np
import pandas as pd

## Missing Data 

# =============================================================================
day = ["Monday","Tuesday","Wednesday"]
# city = ["Bursa","Burdur","Bolu"]
# tempData = np.array([[30,20,40],
#                     [29,np.nan,39],
#                     [np.nan,25,38]])
# 
# =============================================================================

tempData = {"Bursa": [30,29,np.nan],
            "Burdur":[20,np.nan,25],
            "Bolu"  :[40,39,24]}
dataFrame = pd.DataFrame(data=tempData,
                         index=day)
#dataFrame.dropna() drops the raws which includes nan
#dataFrame.dropna(axis = 1) drops the columns
#dataFrame.fillna(20)
print(dataFrame)
