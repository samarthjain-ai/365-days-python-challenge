#
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Matrix_3x3=np.random.randint(1,100,(3,3))
print("Matrix_3x3 ==>\n",Matrix_3x3)
print("Mean of matrix ==>\n",Matrix_3x3.mean())
print("Transpose of matrix ==>\n",Matrix_3x3.T)
print("flatened ==>\n",Matrix_3x3.flatten())

A=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
print("Reshape ==>\n",A.reshape(4,4))

print("Identity Matrix ==>\n",np.eye(5))

# Pandas
data={
    "Name":["subh","samarth","Bob","jhon","Don","ram","rohit"],
    "Department":["AI","HR","IT","IT","AI","AI","HR"],
    "Marks":[90,56,25,86,89,32,67],
    "City":["Indore","Bhopal","Indore","Mumbai","Bhopal","Indore","Indore"]
}
df=pd.DataFrame(data)
print("Top 5 ==>\n",df.head())
print("last 5 ==>\n",df.tail())
print("shape ==>\n",df.shape)
print("Columns name ==>\n",df.columns)

print("Marks greater then 75 ==>\n",df[df["Marks"]>75])

print("Avarage Marks department wise ==>\n",df.groupby("Department")["Marks"].mean())
print(df.sort_values("Marks", ascending=False))

print("Count department ==>\n",df["Department"].value_counts())


data1={
    "Name":["subh","samarth","Bob","jhon","Don","ram","rohit"],
    "Department":["AI","HR","IT","IT","AI","AI","HR"],
    "Marks":[90,56,25,86,None,None,67],
    "City":["Indore","Bhopal","Indore","Mumbai","Bhopal","Indore","Indore"]
}
df_1=pd.DataFrame(data1)

print("info ==>\n",df_1.info())
print("Null value ==>\n",df_1["Marks"].isnull())
print("Null value count ==>\n",df_1["Marks"].isnull().sum())
print("Full the null values ==>\n",df_1["Marks"].fillna(df["Marks"].mean()))
print("Duplicate check ==>\n",df_1.duplicated())
print("Duplicate count ==>\n",df_1.drop_duplicates())

C_M=df.groupby("City")["Marks"].mean()
plt.bar(C_M.index,C_M.values,color=["LightGreen","LightBlue","Yellow"])
plt.show()

D_M=df.groupby("Department")["Marks"].mean()
plt.scatter(D_M.index,D_M.values,c=D_M.values,cmap="cool")
plt.show()

