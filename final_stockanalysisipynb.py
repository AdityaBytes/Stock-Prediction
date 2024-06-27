# -*- coding: utf-8 -*-
"""Final_Stockanalysisipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ECduA-TcaHCzfrzY6tBMiazk-Iu7JL7s
"""

from datetime import datetime
import tensorflow as tf
from tensorflow import keras
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import numpy as np
import seaborn as sns

import pandas as pd
data= pd.read_csv("MicrosoftStock.csv")
data.head()
data.dropna()
data_num= data.select_dtypes(include=np.number)

data.shape

data.isnull().any()

data.info()

data.describe()

import matplotlib.pyplot as plt
from datetime import datetime
plt.plot(data['date'],data['open'],color="blue",label="open")
plt.plot(data['date'],data['close'],color="green",label="close")
plt.title("Microsoft Open-close Stock")
plt.legend()
plt.grid()

plt.plot(data['date'],data['volume'])
plt.show()

sns.heatmap(data_num.corr(),
			annot=True,
			cbar=False)
plt.show()

data['date'] = pd.to_datetime(data['date'])
prediction = data.loc[(data['date'] > datetime(2013, 1, 1)) & (data['date'] < datetime(2018, 1, 1))]
plt.figure(figsize=(12,6))
plt.plot(prediction['date'], prediction['close'], color='r', label='Close Price')
plt.xlabel("Date", fontsize=12)
plt.ylabel("Close Price", fontsize=12)
plt.title("Microsoft Stock Prices (2013-2018)", fontsize=14)
plt.grid(True)
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

msft_close = data.filter(['close'])
dataset = msft_close.values
training = int(np.ceil(len(dataset) * .95))
ss = StandardScaler()
ss = ss.fit_transform(dataset)
train_data = ss[0:int(training), :]
x_train = []
y_train = []
for i in range(60, len(train_data)):
    x_train.append(train_data[i-60:i, 0])
    y_train.append(train_data[i, 0])
x_train, y_train = np.array(x_train), np.array(y_train)
X_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense

data = {
    'feature1': np.random.rand(100),
    'feature2': np.random.rand(100),
    'output': np.random.rand(100) * 10
}
df = pd.DataFrame(data)

scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(df[['feature1', 'feature2', 'output']])

X = scaled_data[:, :2]
y = scaled_data[:, 2]

X = X.reshape(X.shape[0], 1, X.shape[1])

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = Sequential()
model.add(LSTM(50, input_shape=(X_train.shape[1], X_train.shape[2])))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse')

model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test), verbose=1)

mse = model.evaluate(X_test, y_test)
print("Mean Squared Error:", mse)