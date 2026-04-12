import numpy as np
a=np.arange(4)
print(a)
b=a
c=a
d=b
print(id(a),id(b),id(c),id(d))
a[0]=10
print(a,b,c,d)
print(a is d)
e=np.arange(4)
print(id(e))
h=a.copy()
print(h,id(h),not(a is h))