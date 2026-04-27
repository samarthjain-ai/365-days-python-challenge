# pip install pandas 
# python -m pip install pandas
# import pandas as pd -- where pd is 
import pandas as pd
#Create a series
series=pd.Series([1,2,3,4,5])
print(series)
# series in array 
print("series in array fome , length ==>\n",series.array)
# Index and its datype
print("Index and datype ==> \n",series.index)

# series with index name given
series2=pd.Series([10,20,30,40,50],index=["A","B","C","D","E"])
print("Series with index ==>\n",series2)
print("Index ==>\n",series2.index)

# calling by index
print("calling by index ==>\n",series2["C"])

# update by index
series2["C"] = 6
print("update by index ==>\n",series2)

# Boolean 

print("Greater then 20 ==>\n",series2[series2>20])
print("smaller then 20 ==>\n",series2[series2<20])

# use of in
print("Is B in series2 ==>\n","B" in series2)
print("is S in series2 ==>\n","S" in series2)

# dic to series
data = {
    "a":100,
    "b":200,
    "c":300,
    "d":400,
    "e":500
}

series3=pd.Series(data)
print("Series from dic ==> \n",series3)

# series to dic
print("Series to dic ==> \n",series2.to_dict())

# converting the index
d= ["x","y","a","b","c"]
series4 = pd.Series(data,index=d)
print(series4)

# isna and notna -- use to detect missing data
print("By use of isan ==> \n",pd.isna(series4))   #NAN = true
print("By use of notan ==> \n",pd.notna(series4))  #NAN = false

# arithmetic operations

print("Series 3 ==>\n",series3)
print("Series 4 ==>\n",series4)

print("Adding of two series ==> \n",series3+series4)
print("x of two series ==> \n",series3*series4)
print("Sub of two series ==> \n",series3-series4)
print("Devide of two series ==> \n",series3/series4)
print("modulo of two series ==> \n",series3%series4)

# naming 
series4.name="A_to_Z"
print(series4)
series4.index.name = "a_z"
print(series4)