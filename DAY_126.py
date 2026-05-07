# 
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("sales_data.csv")
print("Given data : \n",data)

# Adding new coloum
# Task1
data["total_sales"]=data["price"]*data["quantity"]
print("Added Total sales :\n",data)

# Task2
print("Top 3 are :\n",data.sort_values("total_sales",ascending=False).head(3))

# Task3
print("Total sales by category :\n",data.groupby("category")["total_sales"].sum())

# Task4
print("City with highest total sales :\n",data.groupby("city")["total_sales"].sum())

# Task5
print("products greater then 4.5 rating AND price < 30000 ==> \n",data[(data["rating"]>4.5) & (data["price"]<30000)])

# Task6
print("Average rating per category : \n",data.groupby("category")["rating"].mean())

# Task7
print("correlation between price,quantity,rating,total sales :\n",data[["price","quantity","rating","total_sales"]].corr())

# Task8
# Bar graph

plt.bar(data["rating"],data["total_sales"])
plt.title("rating VS total_sales")
plt.xlabel("rating")
plt.ylabel("sales")
plt.legend()
plt.show()

plt.scatter(data["category"],data["total_sales"])
plt.title("category VS total_sales")
plt.xlabel("category")
plt.ylabel("sales")
plt.show()