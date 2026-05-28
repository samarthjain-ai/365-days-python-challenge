#
import  numpy as np
import pandas as pd

N=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
N_1=N.reshape(3,5)
print(N_1.T)
print(N_1[N_1>7])

#
data={
    "Name":["Samarth","Bob","Riya"],
    "Marks":[90,45,78]
}

df=pd.DataFrame(data)
print(df[df["Marks"]>50])
print(df["Marks"].mean)
print(df["Marks"].sort_values(ascending=False))