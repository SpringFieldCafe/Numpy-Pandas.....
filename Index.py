import numpy as np

A=np.arange(3,15)
print(A)
print(A[3])
B=A.reshape(3,4)
print(B,A)
print(B[2])
print(B[2][1])
print(B[2,1])
print(B[2,1:3])
print(B[:,1])

for row in B:
    print(row)

for column in B.T:
    print(column)

for item in B.flat:
    print(item)

