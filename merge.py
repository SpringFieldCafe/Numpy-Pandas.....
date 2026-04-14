import numpy as np
import pandas as pd

left=pd.DataFrame({'key':['K0','K1','K2','K3'],
                   'A':['A0','A1','A2','A3'],
                   'B':['B0','B1','B2','B3']})

right=pd.DataFrame({'key':['K0','K1','K2','K3'],
                    'C':['C0','C1','C2','C3'],
                    'D':['D0','D1','D2','D3']})

# print(left)
# print(right)

re=pd.merge(left,right,on='key')
print(re)

d1=pd.DataFrame({'key1':['K0','K0','K1','K2'],
                 'key2':['K0','K1','K0','K1'],
                 'A':['A0','A1','A2','A3'],
                 'B':['B0','B1','B2','B3']})

d2=pd.DataFrame({'key1':['K0','K1','K1','K2'],
                'key2':['K0','K0','K0','K0'],
                'C':['C0','C1','C2','C3'],
                'D':['D0','D1','D2','D3']})

re2=pd.merge(d1,d2,on=['key1','key2'],how='inner')
re3=pd.merge(d1,d2,on=['key1','key2'],how='outer')
re4=pd.merge(d1,d2,on=['key1','key2'],how='left')
# print(re2)
# print(re3)
# print(re4)

df7=pd.DataFrame({'col1':[0,1],'col_left':['a','b']})
df8=pd.DataFrame({'col1':[1,2,2],'col_right':[2,2,2]})
# print(df7)
# print(df8)

r123=pd.merge(df7,df8,on='col1',how='outer',indicator=True)
r12=pd.merge(df7,df8,on='col1',how='inner',indicator=True)
r42=pd.merge(df7,df8,on='col1',how='outer',indicator='id_co')
# print(r123)
# print(r12)
# print(r42)

i1=pd.DataFrame({'A':['A0','A1'],
                 'B':['B0','B1']},
                 index=['K1','K2'])
i2=pd.DataFrame({'C':['C0','C1'],
                 'D':['D0','D1']},
                 index=['K2','K4'])

re1=pd.merge(i1,i2,left_index=True,right_index=True,how='outer')
print(re1)

b=pd.DataFrame({'k':['k0','k1','k2'],'age':[1,2,3]})
g=pd.DataFrame({'k':['k0','k0','k3'],'age':[4,5,6]})

ba=pd.merge(b,g,on='k',suffixes=['_boy','_girl'],how='inner')
print(ba)