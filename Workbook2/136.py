import numpy as np

a = np.arange(25).reshape(5, 5)
print(f"Форма: {np.shape(a)}\nРазмер: {np.size(a)}\nРазмерность: {np.ndim(a)}")
