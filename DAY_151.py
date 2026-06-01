import numpy as np

A = np.random.randint(1,100,(4,4))

print(A)
print(A.max())
print(A.min())
print(A.mean())
print(A.flatten())
print(A.reshape(2,8))
print(A.T)

data = {
    "Name":["Samarth","Bob","Riya","Jhon","Rohit"],
    "Department":["AI","HR","AI","IT","AI"],
    "Marks":[90,45,None,56,67]
}

import pandas as pd

df=pd.DataFrame(data)
print(df)
print(df.info())
print(df.head())
print(df.tail())
print(df.describe())
print(df.isnull().sum())
df["Marks"]=df["Marks"].fillna(35)
print(df["Marks"])
print(df.groupby("Department")["Marks"].mean())
print(df.groupby("Department")["Marks"].value_counts())

import matplotlib.pyplot as plt
department_avg = df.groupby("Department")["Marks"].mean()
plt.bar(department_avg.index,department_avg.values)
plt.title("Department vs avarage marks")
plt.xlabel("Department")
plt.ylabel("Avarage marks")
plt.show()