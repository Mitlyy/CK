import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from numpy import *


d = []
for i in range(1, 5):
    temp = Image.open('Masks/%d.png' % i)
    img = temp.convert('L')
    img = asarray(img)
    print(img+1000)

plt.imshow(img)

plt.show()
