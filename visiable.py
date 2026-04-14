import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

d=pd.Series(np.random.randn(100),index=np.arange(100))


df=pd.DataFrame(np.random.randn(100,4),index=np.arange(100),columns=list("abcd"))
df=df.cumsum()
ax=df.plot.scatter(x='a',y='b',color='DarkBlue',label='Class 1')
df.plot.scatter(x='a',y='c',color='DarkGreen',label='Class 2',ax=ax)
plt.show()

