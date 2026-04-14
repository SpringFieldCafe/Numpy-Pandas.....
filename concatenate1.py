import numpy as np
import pandas as pd

# d=pd.read_sql('第一次sql.sql')
# print(d)

df1=pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','e'])
df2=pd.DataFrame(np.ones((3,4))*3,columns=['a','b','c','d'])
df3=pd.DataFrame(np.ones((3,4))*5,columns=['a','b','c','f'])
print(df1)
print(df2)
print(df3)

l=pd.merge(df1,df2,on=['a'],how='outer')
print("l::::\n",l)

res=pd.concat([df1,df2,df3],axis=0)
print(res)

df4=pd.DataFrame(np.ones((3,4))*5,columns=['a','b','c','d'])
re=pd.concat([df2,df4])
print(re)

re1=pd.concat([df1,df2,df3],ignore_index=True)
print(re1)

d1=pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'],index=[1,2,3])
d2=pd.DataFrame(np.ones((3,4))*5,columns=['a','d','f','h'],index=[2,5,6])
r1=pd.concat([d1,d2],axis=0,join='outer')
r3=pd.concat([d1,d2],axis=1,join='outer')
r2=pd.concat([d1,d2],join='inner')
r4=pd.concat([d1,d2],axis=1,join='inner')
r5=pd.concat([d1,d2])
print("r1:",r1)
print(r3)
print("r2:",r2)
print(r4)
print(r5)

# df5=pd.concat([d1,d2],axis=1,join_axes=[df1.index])


rt=d1.append(df2)
print(rt)