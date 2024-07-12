import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use('TkAgg')
a = np.array((1, 1, 1))
b = np.array((3, 3, 3))
c = np.array((2, 2, 2))
d = np.array((4, 4, 4))
print("Расстояние между:\nA и B: ", np.linalg.norm(b - a), "\nA и С: ", np.linalg.norm(c - a), "\nA и D: ",
      np.linalg.norm(d - a),
      "\nB и C: ", np.linalg.norm(c - b), "\nB и D: ", np.linalg.norm(d - b), "\nC и D: ",
      np.linalg.norm(d - c))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(a[0], a[1], a[2])
ax.scatter(b[0], b[1], b[2])
ax.scatter(c[0], c[1], c[2])
ax.scatter(d[0], d[1], d[2])
plt.show()
