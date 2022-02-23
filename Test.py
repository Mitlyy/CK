
import numpy as np
from pandas import Series, DataFrame
import pandas as pd

A = {'Животное':['Собака', 'Кошка', 'Лис'],
     'Цвет':['Белая', 'Серый', 'Рыжий'],
     "Сила":[150, 80, 90]}
DA = DataFrame(A, columns=['Цвет', "Сила"],
               index=A['Животное'])
print(DA)
Drop = DA.drop('Собака')
print(Drop)
Drop.reset_index(inplace=True)
df = Drop.rename(columns={'index':'Животное'})
print(Drop)

