import pandas as pd
import matplotlib.pyplot as plt 

data =pd.read_csv("netflix_titles.csv")

print(data.head())
print(data.tail())
print(data.info())
print(data.describe())
print(data.describe(include="all"))
print(data.columns)

print(data.isnull().sum())
data.dropna(subset=["director","cast","country","rating","duration"],inplace=True)
data["rating"].fillna("Unknown")
print("After Removing the all null values ")
print(data.isnull().sum())


DT_count=data["type"].value_counts()
print(DT_count)


plt.pie(DT_count.values,labels=DT_count.index,
        autopct='%1.1F%%',
        explode=[0.1,0],
        colors=["Lightblue","Lightgreen"],
        shadow=True,
        frame=True)
plt.show()
