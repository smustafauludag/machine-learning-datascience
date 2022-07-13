#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 12:41:09 2022

@author: mustafauludag
"""

import pandas as pd

dataFrameExel = pd.read_excel("exel.xlsx")
new_frame = dataFrameExel.dropna()
new_frame.to_excel("new_excel.xlsx")