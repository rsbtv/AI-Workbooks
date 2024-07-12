import pandas as pd

url = 'https://raw.githubusercontent.com/akmand/datasets/main/airline_passenger_satisfaction.csv'
dataframe = pd.read_csv(url, on_bad_lines='skip')
print(dataframe.head(2))
print(dataframe.tail(3))
print(dataframe.shape)
print(dataframe.describe())
print(dataframe.iloc[:5])
print(dataframe.loc[:5])
print(dataframe[dataframe['type_of_travel'] == 'Personal Travel'].head(2))
