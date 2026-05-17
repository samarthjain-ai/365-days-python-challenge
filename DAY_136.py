import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

A=np.array([1,2,3,4,5,6,7,8,98])
A_1=A.reshape(3,3)
print(A_1)
print(A_1.flatten())
print(np.linspace(10,100,10))
print(np.eye(5))

data={
    "Id":["1a","2a","3a","4,a","5a","6a"],
    "Age":[12,34,5,None,77,55]
}

df=pd.DataFrame(data)

print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df["Age"].fillna(df["Age"].mean()))
print(df.groupby("Id")["Age"].mean())