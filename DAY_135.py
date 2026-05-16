
# THEORY REVISION

# NumPy - It is a Python library used for numerical calculations.
# Pandas - It is a Python library used for data analysis in tabular form.
# Matplotlib - It is a Python library used for data visualization.
# Data Cleaning - Process of handling missing values, duplicates, and incorrect datatypes.
# EDA - Exploratory Data Analysis is the process of understanding data.
# DataFrame - A 2D tabular data structure with rows and columns.
# Series - A 1D data structure in pandas.

# PANDAS REVISION

import pandas as pd

Student = {
    "Name":["Samarth","Bob","Ram","Rohit","Subh","Jhon","Riya"],
    "Marks":[89,78,56,None,32,12,90],
    "Department":["AI","IT","AI","IT","HR","HR","AI"],
    "Salary":[100000,20000,40000,53000,60000,70000,800000]
}

data = pd.DataFrame(Student)

print("HEAD ==> \n", data.head())

print("TAIL ==> \n", data.tail())

print("INFO ==> \n")
print(data.info())

print("COLUMNS ==> \n", data.columns)

print("DESCRIBE ==> \n", data.describe())

print("VALUE COUNTS ==> \n",
      data["Department"].value_counts())

print("SHAPE ==> \n", data.shape)

print("NULL VALUES ==> \n", data.isnull())

print("DUPLICATES ==> \n", data.duplicated())

# FILL NULL VALUES

data["Marks"] = data["Marks"].fillna(
    data["Marks"].mean()
)

print("AFTER FILLNA ==> \n")
print(data.info())

# GROUPBY

print(
    "MAX SALARY BY DEPARTMENT ==> \n",
    data.groupby("Department")["Salary"].max()
)

# CORRELATION

print(
    "CORRELATION ==> \n",
    data[["Marks","Salary"]].corr()
)

# NUMPY REVISION

import numpy as np

m = np.array([1,2,33,4,56,7,65,45,34])

print("RESHAPE ==> \n", m.reshape(3,3))

M = np.array([
    [[1,23,3],
     [23,34,43],
     [343,34,3232]]
])

print("FLATTEN ==> \n", M.flatten())

print("LINSPACE ==> \n", np.linspace(1,10,5))

Matrix_5x5 = np.random.randint(1,1000,(5,5))

print("5x5 MATRIX ==> \n", Matrix_5x5)

print("IDENTITY MATRIX ==> \n", np.eye(5))

# VISUALIZATION

import matplotlib.pyplot as plt

data_marks_department = (
    data.groupby("Department")["Marks"].max()
)

plt.bar(
    data_marks_department.index,
    data_marks_department.values
)

plt.title("Department vs Maximum Marks")

plt.xlabel("Department")

plt.ylabel("Maximum Marks")

plt.show()