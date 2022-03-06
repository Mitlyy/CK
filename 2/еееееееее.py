import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from numpy import *


temp = Image.open('%d.png' % 2)
img_1 = temp.convert('L')
img_1 = asarray(img_1)
temp = Image.open('Dva.png').convert('L')
img_2 = temp.convert('L')
img_2 = asarray(img_2)

ImG = img_1 + img_2
plt.imshow(img_1)
plt.show()