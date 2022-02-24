import numpy as np
from pandas import Series, DataFrame
import pandas as pd
report1 = pd.read_csv('1.csv',
                      delimiter=";",
                      )
                      #тут можно сделать сетиндексили так index_col=('REGIONS') )

report1 = report1.set_index('REGION') #Делаю колонку региона индексом
print(report1)

dr = report1.drop(['Сахалинская обл.',
                    "Псковская область",
                    "Приморский край",
                    "Мурманская обл."])
d = dr.sort_values("SALARY")
print(d)
d.reset_index(inplace=True) #d.reset_index("что вместо индекса", inplace=True)
d = d.rename(columns={'index':'REGION'})
print(d)




