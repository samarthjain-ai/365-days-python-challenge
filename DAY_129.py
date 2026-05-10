# DAY 129
import pandas as pd
data=pd.read_csv("supermarketsales.csv")

print("starting 5 rows are :\n",data.head())
print("last 5 rows are     :\n",data.tail())
print("shape of data set   :\n",data.shape)
print("columns name        :\n",data.columns)
print("Info                :\n",data.info())
print("Describe            :\n",data.describe())

print("check num           :\n",data.isnull().sum())
print("duplicated          :\n",data.duplicated())
print("data types          :\n",data.dtypes)


data["check_total"]=data["Unit price"]*data["Quantity"]+data["Tax 5%"]
print(data["Total"]==data["check_total"])

print("Highest bill :\n",data["Total"].max())
print("Lowest  bill :\n",data["Total"].min())
print("Mean    bill :\n",data["Total"].mean())


print("Product line :\n",data["Product line"].value_counts())

print("highest city with sales     :\n",data.groupby("City")["Total"].sum().idxmax())
print("Best Branch                 :\n",data.groupby("Branch")["Total"].sum().idxmax())
print("Most used payment type      :\n",data.groupby("Payment")["Total"].sum().idxmax())
print("Spend by Gender             :\n",data.groupby("Gender")["Total"].sum().idxmax())
print("Who buy more member/normal  :\n",data.groupby("Customer type")["Total"].sum().idxmax())
print("Highest rating by product line  :\n",data.groupby("Product line")["Rating"].idxmax())
print("Who buy more in members f/m  :\n",data.groupby("Gender")["Customer type"].count())
print(data[["Unit price","Quantity","Total","gross income","Rating"]].corr())

import matplotlib.pyplot as plt

plt.bar(x=data["City"],height=data["Total"],color=["skyblue","orange","green"])
plt.title("City vs Total Sales")
plt.xlabel("City")
plt.ylabel("Total sales")
plt.show()

plt.scatter(data["Unit price"],data["Total"],c=data["Rating"],cmap="viridis")
plt.title("Unit price vs Total")
plt.xlabel("Unit price")
plt.ylabel("Total")
plt.show()

plt.hist(data["Rating"])
plt.title("Ratings distribution")
plt.show()
