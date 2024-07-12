import pandas as pd

url = 'https://raw.githubusercontent.com/akmand/datasets/main/airline_passenger_satisfaction.csv'
dataframe = pd.read_csv(url, on_bad_lines='skip')
print(dataframe)
