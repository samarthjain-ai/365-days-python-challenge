import pandas as pd
# Q5


# Q6 
student_data={
    "Enr.":["25ADV3ARI0001","25ADV3ARI0002","25ADV3ARI0003","25ADV3ARI0004","25ADV3ARI0005",],
    "name":["samart","subh","bob","jhon","maggie"],
    "physics":[82,65,45,89,67],
    "chamistry":[67,78,90,34,23],
    "maths":[90,75,34,23,78]
}
df_student=pd.DataFrame(student_data)
print(df_student)
# 1  find the summery of categorical data
print("summery of categorical data ==>\n",df_student.describe())
# 2 drop enr. column
print("drop enr. column ==>\n",df_student.drop("Enr.",axis=1))
# 3 total marks of each stident
df_student["total_student"]=df_student["physics"]+df_student["chamistry"]+df_student["maths"]
print("total marks of each stident ==>\n",df_student)

# 4 find the marks greater than 75 in each subject
print("marks greater than 75 in physics   ==>\n",df_student[df_student["physics"]>75])
print("marks greater than 75 in chamistry ==>\n",df_student[df_student["chamistry"]>75])
print("marks greater than 75 in maths     ==>\n",df_student[df_student["maths"]>75])
# 5 find unique values in column named chamistry
print("unique values in column chamistry ==>\n",df_student["chamistry"].unique()) 


# Q7 - Describe atleat 8 function of numpy for arry creation and manipulation
import numpy as np
print("1 np.array    ==>\n",np.array([23,43,56,56,67,78,54]))
#Converts a list or tuple into a NumPy array. 0D, 1D , 2D , 3D
print("2 np.Zero     ==>\n",np.zeros([3,4]))
#Creates an array where all elements are 0
print("3 np.ones     ==>\n",np.ones([9,9]))
# Creates an array where all elements are 1
n=int(input("Enter a number here ==> "))
print("4 np.full ==>\n",np.full([3,4],n))
# Create an array where the all element are of given number
print("5 np.eye  ==>\n",np.eye(7))
# Create an identity array of matrix of given number
print("6 np.linspace ==>\n",np.linspace(0,1,5))
#Creates evenly spaced numbers between two limits
a=np.array([1,2,34,5,6,67,])
print("7 reshape ==>\n",a.reshape(2,3))
# Changes dimensions without changing data.
b=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("8 flatten ==>\n",b.flatten())

 

# Q9 create a matrix of 5X5 and do the following functions

matrix_5X5=np.array([[1,2,3,4,5],
                     [6,7,8,9,10],
                     [11,12,13,14,15],
                     [16,17,18,19,20],
                     [21,22,23,24,25]])
print("element grater then 10 ==>\n",matrix_5X5>10)
print("First 2 rows and last two coloums ==>\n",matrix_5X5[0:2,3:5])
print("Transposed the matrix ==>\n",matrix_5X5.T)

# Q10 - Expalin the to full proces of data cleaning in pandas how to do 
# missing values
# duplicate values
# incorrect datatype
# describe functions linke deop,fillna,duplicted,deop-duplicate,astype

# Data cleaning is the process of fixing or
# removing incorrect, corrupted, duplicate, or missing data from a dataset.

data_set={
    "name":["samarth","BOB","oggy","pikchu","kaju"],
    "age":[18,46,np.nan,28,17],
    "marks":[19,12,14,18,20]
}

data=pd.DataFrame(data_set)
print("\n",data)

print("Info ==>\n",data.info())
print("shape ==>\n",data.shape)
print("chake missing values ==>",data.isnull())
print("see where it is ==>\n",data.isnull().sum())  
print("fill the missing values with the mean age ==>\n",data["age"].fillna(data["age"].mean()))
print("describe ==>\n",data.describe())
print("drop ==>\n",data.dropna(subset=["age"],inplace=True))
print(data)
print("Duplicate ==>\n",data.duplicated())
print("remove dupliocate ==>\n",data.drop_duplicates())
print("Incorect data type ==>\n",data.dtypes)
data["marks"] = data["marks"].astype(int)
print("astype ==>\n",data.dtypes)