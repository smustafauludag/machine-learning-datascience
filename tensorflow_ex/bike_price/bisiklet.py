#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 13:11:52 2022

@author: mustafauludag
"""
import seaborn as sbn
import pandas as pd

dataFrame = pd.read_excel("../../datasets/bisiklet_fiyatlari.xlsx")
dataInfo = dataFrame.describe()
#sbn.pairplot(dataFrame)

# =============================================================================
# Seperate test and train
from sklearn.model_selection import train_test_split

# y = ax + b (y=f(x))
# y-> label
y = dataFrame["Fiyat"].values

# x -> features
x = dataFrame[["BisikletOzellik1","BisikletOzellik2"]].values

x_train, x_test, y_train, y_test = train_test_split(x,y,
  test_size=0.33,random_state=15)

# =============================================================================

# =============================================================================
# Scaling
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaler.fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)
# =============================================================================

# =============================================================================
# Modeling
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential()

model.add(Dense(4,activation="relu")) # Hidden Layer
model.add(Dense(4,activation="relu")) # Hidden Layer
model.add(Dense(4,activation="relu")) # Hidden Layer
model.add(Dense(1)) #Output Layer

model.compile(optimizer="rmsprop",loss="mse")

model.fit(x_train,y_train,epochs=250) # Start training

loss = model.history.history["loss"]# Loss History

sbn.lineplot(x=range(len(loss)),y=loss)

trainLoss = model.evaluate(x_train,y_train,verbose=0)
testLoss = model.evaluate(x_test,y_test,verbose=0)
# =============================================================================

# =============================================================================
# Testing - Prediction
from sklearn.metrics import mean_squared_error, mean_absolute_error

testPrediction = model.predict(x_test).reshape(330,) # Predict outputs from model with given vals
predictionDataFrame = pd.DataFrame({"Model Out": testPrediction,"Real Vals": y_test})

mae = mean_absolute_error(predictionDataFrame["Real Vals"],
                          predictionDataFrame["Model Out"])
#real vals = model vals +- mae

mse = mean_squared_error(predictionDataFrame["Real Vals"],
                         predictionDataFrame["Model Out"])

sbn.scatterplot(x="Real Vals", y= "Model Out",data=predictionDataFrame)
# =============================================================================

# =============================================================================
# Predict bisiklet fiyat
newBikeFeatures = [[1750.02,1749.96]]
newBikeFeatures = scaler.transform(newBikeFeatures)
newBikePredPrice = model.predict(newBikeFeatures)
# =============================================================================

# =============================================================================
# Save the model
from tensorflow.keras.models import load_model
model.save("bisiklet_modeli.h5") # Save the model
newModel = load_model("bisiklet_modeli.h5") # import the model
# =============================================================================






