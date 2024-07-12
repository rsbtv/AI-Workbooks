import pandas as pd
from numpy import sqrt

a = list(input("Введите координаты XYZ для точки A: "))
b = list(input("Введите координаты XYZ для точки B: "))
a = list(map(int, a))
b = list(map(int, b))
a = pd.Series(a, ['x', 'y', 'z'])
b = pd.Series(b, ['x', 'y', 'z'])
distance = sqrt(((a['x'] - b['x']) ** 2) + ((a['y'] - b['y']) ** 2) + ((a['z'] - b['z']) ** 2))
print(distance)
