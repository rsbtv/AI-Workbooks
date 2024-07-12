import matplotlib
from matplotlib import pyplot as plt
from numpy import sqrt, e, cos, sin, log

matplotlib.use('TkAgg')


def func(x):
    return (sqrt(1 + e ** sqrt(x) + cos(x ** 2)) / abs(1 - (sin(x) ** 3))) + log(abs(2 * x))


answers = [func(x) for x in range(1, 11)]
half_answers = answers[:5]

# Линейный график
plt.plot(range(1, 11), answers)
plt.grid()

# Точечный график
fig = plt.figure(figsize=(8, 4))
plt.scatter(range(1, 6), half_answers)
plt.grid()
plt.show()
