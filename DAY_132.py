import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
A=(Arr.reshape(3,4))
print(A)
print(A.flatten())

print("5x5 matrix ==>\n",np.random.randint(1,100,(5,5)))
N=np.random.randint(1,100,10)
print(N.max())
print(N.mean())
print(N.min())

data ={
    "name":["samarth","subh","BOB","jhon","maggi"],
    "age":[14,23,34,67,87],
    "salary":[2000,4000,450,340,230],
    "Department":["AI","IT","AI","IT","HR"]
}
D=pd.DataFrame(data)
print(D.head(3))
print(D.tail(2))
print(D.shape)
print(D.columns)

print(D["age"]>50)
print(D.groupby("Department")["age"].mean())
