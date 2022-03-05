import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from numpy import*

for i in range(1, 10):
    temp = asarray(Image.open('Masks\1.png' %i))

plt.imshow(temp*10)

plt.show()


