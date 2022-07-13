#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 10:57:33 2022

@author: mustafauludag
"""

import pandas as pd
import numpy as np

rawData = pd.read_excel("../../datasets/maliciousornot.xlsx")
rawDataInfo = rawData.describe()
print(rawData.isnull().sum())

coralation = rawData.corr()["Type"].sort_values()
coralation.plot(kind="bar")

elData = rawData


# =============================================================================
# Spilt data
from sklearn.model_selection import train_test_split
y = elData["Type"].values
x = elData.drop("Type",axis=1).values
x_train, x_test, y_train, y_test = train_test_split(x,y,
  test_size=0.2,random_state=15)
# =============================================================================


# =============================================================================
# Scale
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)
# =============================================================================


# =============================================================================
# Modeling Classification
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.callbacks import EarlyStopping
model = Sequential()

model.add(Dense(30,activation="relu")) # Hidden Layer
model.add(Dense(15,activation="relu")) # Hidden Layer
model.add(Dense(15,activation="relu")) # Hidden Layer
model.add(Dense(1,activation="sigmoid")) #Output Layer

model.compile(optimizer="adam",loss="binary_crossentropy")

model.fit(x=x_train, y=y_train, validation_data = (x_test,y_test),
  epochs=700,verbose=1) # Start training

loss = pd.DataFrame(model.history.history)# Loss History
loss.plot()

# =================================Early Stopping==============================

earlyStopping = EarlyStopping(monitor="val_loss",mode = "min",verbose=1,patience=25)
model = Sequential()

model.add(Dense(30,activation="relu")) # Hidden Layer
model.add(Dense(15,activation="relu")) # Hidden Layer
model.add(Dense(15,activation="relu")) # Hidden Layer
model.add(Dense(1,activation="sigmoid")) #Output Layer

model.compile(optimizer="adam",loss="binary_crossentropy")
model.fit(x=x_train, y=y_train, validation_data = (x_test,y_test),
  callbacks = [earlyStopping] ,epochs=700,verbose=1) # Start training

lossES = pd.DataFrame(model.history.history)# Loss History
lossES.plot()

# =====================================Dropout=================================
model = Sequential()

model.add(Dense(30,activation="relu")) # Hidden Layer
model.add(Dropout(0.5))
model.add(Dense(15,activation="relu")) # Hidden Layer
model.add(Dropout(0.5))
model.add(Dense(15,activation="relu")) # Hidden 
model.add(Dropout(0.5))
model.add(Dense(1,activation="sigmoid")) #Output Layer

model.compile(optimizer="adam",loss="binary_crossentropy")
model.fit(x=x_train, y=y_train, validation_data = (x_test,y_test),
  callbacks = [earlyStopping] ,epochs=700,verbose=1) # Start training

lossESDp = pd.DataFrame(model.history.history)# Loss History
lossESDp.plot()
# =============================================================================


# =============================================================================
# Prediction
from sklearn.metrics import classification_report, confusion_matrix
predictions = model.predict_classes(x_test)

print(classification_report(y_test, predictions))
print("\n")
print(confusion_matrix(y_test, predictions))
# =============================================================================
model.save("classification_ex_ed_dp05.h5")
