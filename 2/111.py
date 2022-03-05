import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

report1 = pd.read_csv('.csv', header=None)
print(report1)
report1 = np.mat(report1)
x = np.mat(report1)
z = (1/len(report1)) * (x.T*x)
print(z)
w, v = np.linalg.eig(z)
print(v.T[1])
print(report1*v.T[1].T)

flip = np.flip(v, axis=1)
g = np.dot(x, flip)
print(g)
print(np.shape(g))
plt.scatter(np.array(g[:, 0]), np.array(g[:, 1]))
plt.show()

