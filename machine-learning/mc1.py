#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 15:13:36 2022

@author: mustafauludag
"""

import pandas as pd
import numpy as np

rawData = pd.read_csv("../datasets/veri.csv")
rawDataInfo = rawData.describe()


# =============================================================================
# put avarage in place of nans
from sklearn.impute import SimpleImputer
nanData = rawData["kilo"].values.reshape(-1,1)
imputer = SimpleImputer(missing_values=np.nan,strategy="mean")
imputer.fit(nanData)
rawData["kilo"] = imputer.transform(nanData)
# =============================================================================


# =============================================================================
# encoder kategorik -> numeric
from sklearn import preprocessing
le = preprocessing.LabelEncoder()
ohe = preprocessing.OneHotEncoder()

countries = rawData["ulke"].values
leArr = le.fit_transform(countries).reshape(-1,1)
oheArr = ohe.fit_transform(leArr).toarray()
newData = pd.DataFrame(oheArr,columns=["fr","tr","us"])
newData = pd.concat([newData,rawData.drop("ulke",axis=1)],axis=1)

sexData = rawData["cinsiyet"].values
sexArr = le.fit_transform(sexData)
newData["cinsiyet"] = sexArr
# =============================================================================


# =============================================================================
# Spilt data
from sklearn.model_selection import train_test_split
y = newData["cinsiyet"].values
x = newData.drop("cinsiyet",axis=1).values
x_train, x_test, y_train, y_test = train_test_split(x,y,
  test_size=0.33,random_state=0)
# =============================================================================

# =============================================================================
# Scale
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)
# =============================================================================




