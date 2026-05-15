# light revision MST-Time Start 
# DataFrame - dataframe is a 2D data which store the data in rows and columns (Tabuler fome)
# Series - it is a 1D data which have only rowes
# groupby()  - groupby make a groups 
# corr()  - corr tell us the corelation between the columns
# fillna()  - fillna fills the null values here na means None / empty Values
# reshape() - reshape aranges the 1D array into te Row and columns fome
# flatten() - flatten make a any array in !D fome

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Matrix_3x3=np.random.randint(1,1000,(3,3))
print("Matrix_3x3 ==> \n",Matrix_3x3)
print("MAX ==>\n",Matrix_3x3.max())
print("MIN ==>\n",Matrix_3x3.min())
print("MEAN ==>\n",Matrix_3x3.mean())
print("Transpose ==>\n",Matrix_3x3.T)

data = {
    "Name":["Samarth","Bob","Jhon","Subh","Ram","Rohit"],
    "Age":[18,34,78,34,2,87],
    "Department":["AI","HR","IT","HR","AI","AI"],
    "Marks":[90,34,56,89,45,23]
}

df=pd.DataFrame(data)
print("Top 5 ==>\n",df.head())
print("Filter marks greater then 80 ==>\n",df[df["Marks"]>80])
print("Group by mean marks ==>\n",df.groupby("Department")["Marks"].mean())
print("Filter marks greater then 80 ==>\n",df.sort_values("Marks", ascending=False))


A_marks=df.groupby("Department")["Marks"].mean()
plt.bar(A_marks.index,A_marks.values)
plt.title("Department vs Average Marks")
plt.xlabel("Department")
plt.ylabel("Average Marks")
plt.show()
