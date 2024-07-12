from numpy import *
from numpy.random import *
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')

delta = 1.0
x = linspace(-5, 5, 11)
print('значения x - ', x)
y = linspace(-5, 5, 11)
print('значения y', y)
x += delta * (rand(11) - 0.5)
# 3 степени
# Нахождение коэффициентов функции вида y = ax^3 + bx^2 + cx + d методом наименьших квадратов
# Задаем вектор  m = [x**3, x, E]
# m = vstack((x ** 3, x ** 2, x, ones(11))).T
m = vstack((x, ones(11))).T
# Находим коэффициенты при составляющих вектора m
s = linalg.lstsq(m, y, rcond=None)[0]

# На отрезке [-5,5]
x_prec = linspace(-5, 5, 101)
# рисуем точки
plt.plot(x, y, 'D')
# рисуем кривую вида y = ax^3 + bx ^2 + cx + d, подставляя из решения коэффициенты s[0], s[1], s[2], s[3]
# plt.plot(x_prec, s[0] * x_prec ** 3 + s[1] * x_prec ** 2 + s[2] * x_prec + s[3], '-', lw=3)
# plt.plot(x_prec, s[0] * x_prec ** 3 + s[1] * x_prec ** 2, '-', lw=3)
plt.plot(x_prec, x_prec, '-', lw=3)
plt.grid()
plt.savefig('полином 3-й степени.png')
plt.show()
