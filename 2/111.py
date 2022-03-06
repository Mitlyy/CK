import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from numpy import *



# def scale(X, x_min, x_max):
#     nom = (X-X.min(axis=0))*(x_max-x_min)
#     denom = X.max(axis=0) - X.min(axis=0)
#     denom[denom==0] = 1
#     return x_min + nom/denom


B_0 = np.mat(pd.read_csv('13_30 - 16_50.csv',
                                delimiter=";",
                                header=None))

G = 0
img_0 = np.zeros([128, 128])
img_2 = np.zeros([128, 128])
for i in range(2, 700):
    temp = Image.open('%d.png' % i)
    img = temp.convert('L')
    img = asarray(img)
    img_0 += img
    G += B_0[i-2, 1]
    img_2 += img*B_0[i-2, 1]

plt.imshow((img_2/i)-(1/i * G * 1/i * img_0))
plt.show()

