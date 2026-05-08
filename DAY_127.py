# Q1 - Define dataFrame in pandas show how it's diifrant from series
# ANSWER - dataframe is the 2D structerd labal data which is stored in the fome of rows and columns
# Example :
import pandas as pd
data ={
    "name":["samarth","subh","bob","jon"],
    "age":[18,34,56,3]
}
df =pd.DataFrame(data)
print(df)
#Differnce
#s  - 1D , same data type      , single column  , only index
#df - 2D , different data type , complete table , have both raw and column index

s = pd.Series([1,2,3,4,5])
print("Series    ==> \n",s)
print("Dataframe ==> \n",df)

# Q2 - writr a python Script to create a 1-D array with numbers 1 to 10
# Then 1-Find mean of these number
#      2-Multiply every number by 2 and print result
import numpy as np

series_2=np.random.randint(0,10,20)  # start/stop-1/how much
print("Series by numpy ==>\n",series_2)
print("mean of series ==>\n",series_2.mean())
print("multipy every number by 2 then print result ==>\n",series_2*2)

# Q3 Explain the loc and iloc in pandas with Examples
# Answer ==> loc is label-based indexing.
#            iloc is integer position-based indexing. 
print("loc  use ==>\n",df.loc[1,"name"])
print("iloc use ==>\n",df.iloc[1,1])

# Q4 parform the following on the data set

data_4={
    "name":["samarth","subh","bob","jhon","don"],
    "age":[18,23,12,45,67],
    "department":["AI","IT","HR","AI","HR"],
    "salary":[10000,20000,50000,25000,12999]
}

print("DATA SET ==>\n",pd.DataFrame(data_4))
# To do -
# Display the front row
print("Front row ==> \n",pd.DataFrame(data_4).head(1))
# rename the column
print("rename the old name with new name ==>\n",pd.DataFrame(data_4).replace("bob","bob the builder"))
