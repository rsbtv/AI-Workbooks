import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')
# Задаем исходные данныые
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

# Строим полином первой степени с помощью функции polyfit
coefficients = np.polyfit(x, y, 1)
poly1d_fn = np.poly1d(coefficients)

# Создаем массив значений для экстраполяции
x_new = np.array([6, 7, 8, 9, 10])

# Получаем экстраполированные значения
y_new = poly1d_fn(x_new)

# Строим график
plt.plot(x, y, 'o', label='Исходные данные')
plt.plot(x_new, y_new, label='Экстраполяция')
plt.legend(loc='best')
plt.show()