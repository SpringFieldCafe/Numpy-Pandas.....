import numpy as np
import pandas as pd
s=pd.Series([1,3,6,np.nan,44])
print(s)
dates=pd.date_range('20260401',periods=6)
print(dates)
df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])
print(df)
df1=pd.DataFrame(np.arange(12).reshape(4,3))
print(df1)
df2=pd.DataFrame({'A':1,
                  'B':pd.Timestamp('20260402'),
                  'D':pd.Categorical(["test","train","test"]),
                  'E':"affaf"})
print(df2,"\n",df2.dtypes)
print(df2.index)
print(df2.columns)
print(df2.values)
print(df2.describe())
print(df2.T)
print((df2.describe()).T)
df2.sort_index(axis=1,ascending=False)
print(df2.sort_index(axis=1,ascending=False))
print(df2.sort_values(by='A'))