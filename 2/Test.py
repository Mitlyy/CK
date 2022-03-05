import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

report1 = pd.read_csv('14_16.csv', header=None)
print(report1)
report1 = np.mat(report1)
print(report1)
d = report1.mean(axis=0)
print('VOT D', d)
report1 = report1 - d
x = report1
z = (1 / len(report1)) * (x.T * x)
print(z)
w, v = np.linalg.eig(z)
print("Долевая дисперсия:", (w[0] + w[1]) / sum(w[0:]), "\n"
      "vectors:", w, '\n'
      "Max vector:", max(w), "\n"
      "Вектор в новых координатах:", (report1 * v.T[1].T)[0])

sort = sorted(w, reverse=True)
i = 0
oy = []
while i <= 10:
    oy = np.append(oy, (sum(sort[0:i]) / sum(sort[0:])))
    i += 1
ox = np.arange(i)
print(oy)
plt.plot(ox, oy)

g = x*v
plt.scatter(np.array(g[:, 1]), np.array(g[:, 2]))
plt.show()

