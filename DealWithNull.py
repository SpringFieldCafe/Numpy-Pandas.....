import numpy as np
import pandas as pd

date=pd.date_range('20250505',periods=9)
column=np.arange(7,1,-1)
df=pd.DataFrame(np.arange(54).reshape((9,6)),index=date,columns=column)
print(df)
df.iloc[3,2]=np.nan
df.iloc[3,3]=np.nan
print(df)
print(df.dropna(axis=0,how='any'))
print(df.dropna(axis=1,how='all'))
print(df.fillna(value=0))
print(df.isnull())
print(np.any(df.isnull()))