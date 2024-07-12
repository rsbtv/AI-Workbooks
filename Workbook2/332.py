import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

data = pd.read_csv('https://raw.githubusercontent.com/akmand/datasets/master/iris.csv')
data_length = data['sepal_length_cm']
data_width = data['sepal_width_cm']

scaler = MinMaxScaler()
scaled_length = scaler.fit_transform([[data_length[i]] for i in range(len(data_length))])

scaler = StandardScaler()
scaled_width = scaler.fit_transform([[data_width[i]] for i in range(len(data_width))])

print(scaled_length, scaled_width)
