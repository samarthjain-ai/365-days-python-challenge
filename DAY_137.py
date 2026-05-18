import numpy as np

m_4=np.random.randint(1,100,(4,4))
print("transpose ==>\n",m_4.T)
print("Max ==>\n",m_4.max())
print("Min ==>\n",m_4.min())
print(m_4.flatten())

import pandas as pd
data={
    "Name":["SUBH","BOB","JHON","SAMARTH","RAM","ROHIT"],
    "Department":["AI","HR","AI","HR","IT","AI"],
    "Marks":[90,45,34,23,56,34],
    "Attendance":[9,5,3,7,8,6]
}

df=pd.DataFrame(data)
print(df.head())
print(df.describe())
print(df["Marks"].fillna(df["Marks"].mean()))
print(df.groupby("Department")["Marks"].mean())
print(df[df["Marks"]>70])

import matplotlib.pyplot as plt

plt.scatter(df["Attendance"],df["Marks"],c=data["Marks"],cmap="cool")
plt.title("Attendence VS Marks")
plt.xlabel("Attendance")
plt.ylabel("Marks")
plt.colorbar(label="Marks")
plt.show()