import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Mat_sh = np.mat(pd.read_csv('mat_schet.csv',
                            delimiter=";",
                            header=None))
Mat_vs = np.mat(pd.read_csv('mat_vesov.csv',
                            delimiter=";",
                            header=None))

Mat_vs_cr = Mat_sh*Mat_vs.T
plt.imshow(Mat_vs_cr)

plt.show()


