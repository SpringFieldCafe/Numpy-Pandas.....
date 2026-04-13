import numpy as np
import pandas as pd

d=pd.read_csv('data-1775649368038.csv')
print(d)

d.to_pickle('city.pickle')

e=pd.read_pickle('city.pickle')
print(e)