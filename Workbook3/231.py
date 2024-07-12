# Для предыдущего примера поэкспериментируйте с параметрами
# классификатора:
# 1. Установите другое количество ближайших соседей (k = 1, 5, 10).
# 2. Установите размер тестовой выборки 15% от всего датасета.
# 3. Постройте графики и оцените качество моделей, проанализируйте
# результаты.
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use('TkAgg')
iris = sns.load_dataset('iris')

X_train, X_test, y_train, y_test = train_test_split(
    # Поскольку iris это pandas-таблица, для нее нужно указывать iloc
    iris.iloc[:, :-1],  # Берем все колонки кроме последней в признаки
    iris.iloc[:, -1],  # Последнюю в целевую переменную (класс)
    test_size=0.2  # Размер тестовой выборки 20%
)
# print(X_train.shape(), X_test.shape(), y_train.shape(), y_test.shape())
print(X_train.head())
print(y_train.head())

# Обучим метод трех ближайших соседей
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# Получим предсказания модели
y_pred = model.predict(X_test)
print(y_pred)
# Покажем на графике, что отражает полученное число.
# Красным цветом обозначены точки, для которых классификация сработала неправильно

plt.figure(figsize=(10, 7))

# Левый график
# plt.subplot(121)
sns.scatterplot(
    data=iris,  # Из этой таблицы нарисовать точки
    x='petal_width', y='petal_length',  # С этими координатами,
    hue='species',  # Для которых цвет определить согласно этому столбцу
    s=70  # размер точек
)
plt.xlabel('Длина лепестка, см')
plt.ylabel('Ширина лепестка, см')
plt.legend(loc=2)  # Добавить легенду
plt.grid()  # добавить сетку

# Перебираем все объекты из теста
for i in range(len(y_test)):
    # Если предсказание неправильное
    if np.array(y_test)[i] != y_pred[i]:
        # то подсвечиваем точку красным
        plt.scatter(X_test.iloc[i, 3], X_test.iloc[i, 2], color='red', s=150)

# качество модели (доля правильно классифицрованных точек)
print(f'accuracy: {accuracy_score(y_test, y_pred) : 3}')

# Правый график аналоигчно
# plt.subplot(122)
# sns.scatterplot(
#     data=iris,
#     x='sepal_width',
#     y='sepal_length',
#     hue='species',
#     s=70
# )
# plt.xlabel('Длина чашелистика, см')
# plt.ylabel('Ширина чашелистика, см')
# plt.legend()
# plt.grid()

plt.show()
