import matplotlib
from numpy import cos, e, log
from matplotlib import pyplot as plt
from scipy.integrate import simps
from numpy import trapz

matplotlib.use('TkAgg')


def func(x):
    return abs(cos(x * e ** (cos(x) + log(x + 1))))


answers = [func(x) for x in range(0, 11)]

area = trapz(answers)
print(area)

# Линейный график
plt.plot(range(0, 11), answers)
plt.fill_between(range(0, 11), answers)
plt.grid()
plt.show()
