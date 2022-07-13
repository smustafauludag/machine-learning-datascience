#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 20:30:00 2022

@author: mustafauludag
"""
import pandas as pd
import seaborn as sbn

rawData = pd.read_excel("../../datasets/merc.xlsx")
rawDataInfo = rawData.describe()


# =============================================================================
# 1- Check missing values
print(rawData.isnull().sum())
# If thre are small amount of missing data we can delete the row
# =============================================================================
pd.DataFrame()

# =============================================================================
# 2- Graphical Analysis
sbn.distplot(rawData["price"]) # Distirbution
#TODO There are few cars with too high prices, we can eliminate them
sbn.countplot(rawData["year"])
# How other features effect the price
priceCoralation = rawData.corr()["price"].sort_values()
sbn.scatterplot(x="mileage", y="price",data=rawData)
# =============================================================================


# =============================================================================
#TODO eiminate the high price cars
# If we take 99% of the data, the elimination will not effect much
# We can order prices then eliminate highest 1%
nEliminateData = round(len(rawData) * 0.01)
elData = rawData.sort_values("price",ascending=False).iloc[nEliminateData:]
elDataInfo = elData.describe()
sbn.distplot(elData["price"])
sbn.scatterplot(x="mileage", y="price",data=elData)
yearPrices = elData.groupby("year").mean()["price"]
# we can eliminate 1970
elData = elData[elData.year != 1970]
elData = elData.drop("transmission",axis=1)
# =============================================================================


# =============================================================================
# Spilt data
from sklearn.model_selection import train_test_split
y = elData["price"].values
x = elData.drop("price",axis=1).values
x_train, x_test, y_train, y_test = train_test_split(x,y,
  test_size=0.2,random_state=10)
# =============================================================================


# =============================================================================
# Scale
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)
# =============================================================================


# =============================================================================
# Modeling
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
model = Sequential()

model.add(Dense(12,activation="relu")) # Hidden Layer
model.add(Dense(12,activation="relu")) # Hidden Layer
model.add(Dense(12,activation="relu")) # Hidden Layer
model.add(Dense(12,activation="relu")) # Hidden Layer
model.add(Dense(12,activation="relu")) # Hidden Layer
model.add(Dense(1)) #Output Layer

model.compile(optimizer="adam",loss="mse")

model.fit(x=x_train, y=y_train, validation_data = (x_test,y_test),
  batch_size = 250, epochs=300) # Start training

loss = pd.DataFrame(model.history.history)# Loss History
loss.plot()
# =============================================================================


# =============================================================================
# Testing
from sklearn.metrics import mean_squared_error, mean_absolute_error

testPrediction = model.predict(x_test) # Predict outputs from model with given vals
predictionDataFrame = pd.DataFrame(
  {"Model Out": testPrediction.reshape(len(testPrediction,)),"Real Vals": y_test})

mae = mean_absolute_error(predictionDataFrame["Real Vals"],
                          predictionDataFrame["Model Out"])
mse = mean_squared_error(predictionDataFrame["Real Vals"],
                         predictionDataFrame["Model Out"])

sbn.scatterplot(x="Real Vals", y= "Model Out",data=predictionDataFrame)

print(elData.iloc[2])
dataIndex100 = elData.drop("price",axis=1).iloc[2].values.reshape(1,-1)
dataIndex100 = scaler.transform(dataIndex100)
pCarPrice = float(model.predict(dataIndex100))
# =============================================================================

model.save("car_prediction.h5") # Save the model












