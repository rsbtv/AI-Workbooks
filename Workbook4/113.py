from numpy.random import *
from numpy import *
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')
# Генерируем случайные x и y
delta = 1.0
x = np.linspace(-5, 5, 11)
y = x ** 2 + delta * (rand(11) - 0.5)
x += delta * (rand(11) - 0.5)

# Записываем данные в файл
x.tofile('x_data.txt', '\n')
y.tofile('y_data.txt', '\n')

# Читаем данные из файлов
x = fromfile('x_data.txt', float, sep='\n')
y = fromfile('y_data.txt', float, sep='\n')

# Нахождение коэффициентов функции вида y = ax^2 = bx + c с методом наименьших квадратов
# Задаем вектор m = [x**2, x, E]
m = vstack((x ** 2, x, ones(11))).T
# Находим коэффициенты при составляющих вектора m
s = np.linalg.lstsq(m, y, rcond=None)[0]

# На отрезке [-5, 5]
x_prec = linspace(-5, 5, 101)
# Рисуем точки
plt.plot(x, y, 'D')
# Рисуем кривую вида y = ax^2 + bx + c, подставляя из решения коэффициенты s[0], s[1], s[2]
plt.plot(x_prec, s[0] * x_prec ** 2 + s[1] * x_prec + s[2], '-', lw=2)
plt.grid()
plt.savefig('парабола.png')
plt.show()
