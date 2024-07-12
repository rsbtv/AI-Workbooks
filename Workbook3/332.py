from sklearn.feature_extraction import DictVectorizer

data_dict = [
    {"Зелёный": 0.4, "Серый": 0.6},
    {'Карий': 0.3, 'Голубой': 0.2, "Серый": 0.5},
    {"Голубой": 0.8, "Серый": 0.2},
    {"Карий": 0.5, "Серый": 0.5}
]
dictvectorizer = DictVectorizer(sparse=False)
features = dictvectorizer.fit_transform(data_dict)
print(features)
