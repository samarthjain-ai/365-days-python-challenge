# pip install pandas 
# python -m pip install pandas
# import pandas as pd -- where pd is 
import pandas as pd
# import numpy as np
#Create a series
series=pd.Series([1,2,3,4,5])
print(series)
# series in array 
print("series in array fome , length ==>\n",series.array)
# Index and its datype
print("Index  ==> \n",series.index)
print("Values ==> \n",series.values)
print("Datype ==> \n",series.dtype)

#Indexing and slicing
print("0 Index value ==> ",series[0])
print("slicing value ==> ",series[1:3]) # 1,2

# series with index name given
series2=pd.Series([10,20,30,40,50],index=["A","B","C","D","E"])
print("Series with index ==>\n",series2)
print("Index ==>\n",series2.index)

# calling by index
print("calling by index ==>\n",series2["C"])

# update by index
series2["C"] = 6
print("update by index ==>\n",series2)

# Conditional Selection

print("Greater then 20 ==>\n",series2[series2>20])
print("smaller then 20 ==>\n",series2[series2<20])

# Use of and , or , nor
#10,20,6,40,50 = series2 
print("AND  &  ==>\n",series2[(series2>5) & (series2<10)])
print("OR   |   ==>\n",series2[(series2>20) | (series2<15)])
print("Nor  ~ ==>\n",series2[~(series2>20)])

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

# iloc and loc

new_series=pd.Series([10,20,30,40,50,60,70,80])
print(new_series)
print(new_series.iloc[3]) # print from index
new_series.index=[1,2,3,4,5,6,7,8]
print(new_series)
print("loc ==> ",new_series.loc[3]) # print from index value,name


# Data Frame 
print(f"========== DATA FRAME ==========\n")

data_1= {
    "name":["samarth","bob","jon","subh","jack","don"],
    "age":["18","20","31","19","9","45"],
    "department":["AI","HR","DS","CFS","IT","HR"],
    "salary":[120000,20000,40000,30000,110000,120000]
}

print("DIC \n",data_1)
dataframe=pd.DataFrame(data_1)
print("DATA FRAME \n",dataframe)

# head and tail
print("TOP 5 by head\n",dataframe.head()) # gives the top 5
print("LAST 5 by tail\n",dataframe.tail()) # gives the last 5

# iloc and iloc
print("iloc ==>\n",dataframe.iloc[0:1,0:5]) # [row,colume]
print("loc  ==>\n",dataframe.loc[5,["name","age"]])

# all from key
print("key values ==>\n",dataframe[["age","name"]])

# drop / left
print("Drop ==>\n",dataframe.drop("age",axis=1))

# dataframe shape and info 
print("shape ==> ",dataframe.shape)
print("info ==> \n",dataframe.info)

#describe
print("describe ==> \n",dataframe.describe())

