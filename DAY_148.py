import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

Matrix_4x4=np.random.randint(1,100,(4,4))
print(Matrix_4x4)
print("Transpose ==>\n",Matrix_4x4.T)
print("Mean  ==>\n",Matrix_4x4.mean())
print("Greater then 50 ==>\n",Matrix_4x4[Matrix_4x4>50])
print("Flatten ==>\n",Matrix_4x4.flatten())

data={
    "Name":["samart","Bob","riya","jhon"],
    "Department":["AI","HR","AI","IT"],
    "Marks":[90,45,78,56]
}
df=pd.DataFrame(data)
print(df)
print("Marks greater then 50 ==>\n",df[df["Marks"]>50])
print("Group by department then mean ==>\n",df.groupby("Department")["Marks"].mean())
print("Arrange the Marks in ascending orders ==>\n",df["Marks"].sort_values(ascending=True))
print("Shape ==>\n",df.shape)
print("columns ==>\n",df.columns)

D_A=df.groupby("Department")["Marks"].mean()

plt.bar(D_A.index,D_A.values)
plt.title("Department vs Average Marks")
plt.xlabel("Department")
plt.ylabel("Average Marks")
plt.show()
