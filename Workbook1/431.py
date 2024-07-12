import numpy as np
import matplotlib
from matplotlib import pyplot as plt

matplotlib.use('TkAgg')

y = (np.random.rand(1, 100))

print(f"Среднее значение: {np.mean(y)} \nМедианное значение: {np.median(y)}")

mean = np.mean(y)
median = np.median(y)

# fig, ax = plt.subplots()
plt.scatter(y, y)
plt.scatter(mean, mean)
plt.scatter(median, median)

plt.show()
