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
data["rating"] = data["rating"].fillna("Unknown")
print("After Removing the all null values ")
print(data.isnull().sum())


DT_count=data["type"].value_counts()
print(DT_count)

plt.figure(figsize=(10,6))
plt.pie(DT_count.values,labels=DT_count.index,
        autopct='%1.1F%%',
        explode=[0.1,0],
        colors=["Lightblue","Lightgreen"],
        shadow=True,
        frame=True)
plt.show()

#

top_country = data["country"].value_counts().head(10)
print(top_country)

plt.figure(figsize=(10,5))
plt.bar(top_country.index,
        top_country.values,)

plt.title("Top 10 Countries on Netflix")
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.xticks(rotation=90)

plt.show()

#

rating_count=data["rating"].value_counts()
print(rating_count)

plt.figure(figsize=(10,5))
plt.bar(rating_count.index,
        rating_count.values)

plt.title("Netflix Ratings")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.xticks(rotation=90)

plt.show()

#

print(data["release_year"].max())
print(data["release_year"].min())

release_count = data["release_year"].value_counts()
print(release_count)

plt.figure(figsize=(10,5))
plt.hist(data["release_year"],
         bins=20)

plt.title("Netflix Release Year Distribution")
plt.xlabel("Release Year")
plt.ylabel("Count")

plt.show()

#
genre_count = data["listed_in"].value_counts().head(10)
print(genre_count)

plt.figure(figsize=(10,5))
plt.bar(genre_count.index,
        genre_count.values)

plt.xticks(rotation=90)
plt.title("Top 10 genre on netflix")
plt.xlabel("Genre")
plt.ylabel("Count")

plt.show()

#
director_count = data["director"].value_counts().head(10)
print(director_count)

plt.figure(figsize=(12,6))

plt.bar(director_count.index,
        director_count.values)

plt.title("Top 10 Directors on Netflix")
plt.xlabel("Director")
plt.ylabel("Number of Titles")
plt.xticks(rotation=90)
plt.show()
#

india = data[data["country"] == "India"]

print(india.shape)
print(india["type"].value_counts())
print(india["rating"].value_counts())