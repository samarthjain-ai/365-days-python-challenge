#
import pandas as pd
df = pd.read_csv("student_data.csv")

print("First 2 rows\n")
print(df.head())

print("Columns\n")
print(df.columns)

print("Shape \n")
print(df.shape)

print("Info \n")
df.info()

#Average final marks
print("Average Final marks => ",df["G3"].mean())

#Highest marks
print("Highest Marks => ",df["G3"].max())

#Top student
print(df[df["G3"]>18])

#Average by study time 
print(df.groupby("studytime")["G3"].mean())

