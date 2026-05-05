# pandas function on student_data.csv
import pandas as pd
import matplotlib.pyplot as plt

df =pd.read_csv("student_data.csv")

print(".head take the top 5 row and coloum from the data set \n",df.head())
print(".tail takes the last 5 row and coloum from the data set \n",df.tail())

print(".shape it tell the number of row and coloums in data set \n",df.shape)

print(".isnull it finds the null values in the data set and mark them (false means not null and true means null)==> \n",df.isnull())
print(".isnull().sum() it finds the null values and count/sum and tell us how many is null ()==> \n",df.isnull().sum())


print(".sort_values it arranges the value in ascending fome and ascending ='False'=decending ==>\n",df.sort_values("G3",ascending=False).head(10))

print("Weak students who's marks is less then 8 \n",df[df["G3"]<8])

print("correlation - a relation between the elements that how much i effect the other ",df[["studytime","absences","failures","G3"]].corr())

df.plot.scatter(x="studytime",y="G3")
plt.title("Study Tme vs final marks")
plt.show()