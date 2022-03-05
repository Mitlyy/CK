import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

report1 = np.array([[9, 19], [6, 22], [11, 27], [12, 25], [7, 22]])
print(report1)
d = report1.mean(axis=0)
print(d)
report1 = report1 - d
print(report1)
x = np.mat(report1)
z = (1/len(report1)) * (x.T*x)
print(z)
w, v = np.linalg.eig(z)
print(v.T[1])
print(report1*v.T[1].T)



