import pandas as pd
import matplotlib.pyplot as plt

data =pd.read_csv("Coffe_sales.csv")

print("Top  5 rows ==> \n",data.head())
print("Last 5 rows ==> \n",data.tail())
print("INFO        ==> \n",data.info())
print("Columns Names ==> \n",data.columns)
print("Shape         ==> \n",data.shape)
print("describe Numrical columns ==> \n",data.describe())
print("describe Catogorical data ==> \n",data.describe(include="string"))
print("Shape ==> \n",data.shape)
print("Dtype ==> \n",data.dtypes)
print("index    ==> ",data.index)
print("LOC Row 0")
print(data.loc[0])

print("\nLOC Rows 0 to 4")
print(data.loc[0:4])

print("\nILOC Row 0")
print(data.iloc[0])

print("\nILOC Rows 0 to 4")
print(data.iloc[0:5])

print("Null values ==> \n",data.isnull())
print("Numbers of the null colunms ==> ",data.isnull().sum())
print(data.fillna(35))
print(data.dropna())

print(data["coffee_name"])
print(data[["coffee_name","money"]])


print(data[data["money"]>30])
print(data[data["money"]==35.76])
print(data["money"].sort_values())
print(data["money"].sort_values(ascending=False))
# unique()

print(data["coffee_name"].value_counts())
# print("Coffee" in data["product"].values)
print(data.groupby("coffee_name")["money"].mean())
print(data.groupby("coffee_name")["money"].max())
print(data.groupby("coffee_name")["money"].min())
print(data.groupby("coffee_name")["money"].count())

print(data.drop(columns="coffee_name"))

print("\nUnique Coffee Names")
print(data["coffee_name"].unique())

coffee = input("Enter coffee name: ")

print(coffee in data["coffee_name"].values)

new_data = data.reindex(range(len(data)+5))
print(new_data)

print(data["money"] + 5)
print(data["money"] * 2)

updated_money = data["money"].apply(lambda x: x + 10)
print(updated_money)

print(data["money"].rank())

print(data.corr(numeric_only=True))

print(data.cov(numeric_only=True))

data.to_csv("new_coffee_sales.csv", index=False)

print("\nNew CSV Created Successfully")