import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

report1 = pd.read_csv('14_16.csv', header=None)
print(report1)
d = report1.median()
print(d)
i = 0
while i < len(report1.columns):
    report1[i] = report1[i] - int(d.loc[i])
    i += 1
print(report1)
x = np.mat(report1)
print(x)
z = (1/len(report1)) * (x.T*x)
w, v = np.linalg.eig(z)


