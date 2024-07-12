import numpy as np

size = 6
a = np.zeros((size, size))
a[0] = np.ones(size)
a[size - 1] = np.ones(size)
for i in range(1, size - 1):
    a[i][0] = 1
    a[i][size - 1] = 1

print(a)
