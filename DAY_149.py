import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

Matrix_5x5=np.random.randint(1,100,(5,5))
print(Matrix_5x5)
print("Max  value ==> ",Matrix_5x5.max())
print("Min  value ==> ",Matrix_5x5.min())
print("Mean value ==> ",Matrix_5x5.mean())
print("Transpose  ==> ",Matrix_5x5.T)
print("Values divisible by 2 ==> ")
print(Matrix_5x5[Matrix_5x5 % 2 == 0])

data={
    "Name":["samarth","Bob","Riya","jhon","Rohit"],
    "Department":["AI","HR","AI","IT","AI"],
    "Marks":[90,48,78,56,67],
    "City":["Indore","Bhopal","Indore","Mumbai","Bhopal"]
}
df=pd.DataFrame(data)
print(df)

print("Studednt Marks > 60 ==> ",df[df["Marks"]>60])
print("Average marks city-wise ==> ",df.groupby("City")["Marks"].mean())
print("Average marks department-wise ==> ",df.groupby("Department")["Marks"].mean())
print("Sort marks descending  ==> ",df["Marks"].sort_values(ascending=False))
print("Count students in each department   ==> ",df.groupby("Department")["Department"].count())


d=df["Department"].value_counts()
plt.pie(d.values, labels=d.index, autopct="%1.1f%%")
plt.title("Students per Department")
plt.show()