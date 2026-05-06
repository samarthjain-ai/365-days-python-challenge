import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("employees.csv")
print(data)

# Task 1
print("First 5 rows : \n",data.head())
print("last  3 rows : \n",data.tail(3))
print("Shape : \n ",data.shape)
print("Colume names : \n",data.columns)

# Task 2 
print("Show only name , salary  , department : \n",data[["department","salary","name"]])

#task 3
print("Employees whose salary is greater than 55000 : \n",data[data["salary"]>55000])

#Task 4
print("show the employees whose department is AI :\n ",data[data["department"]=="AI"])

#Task 5
print("Sort the employees by salary in descending order : \n",data.sort_values("salary",ascending=False))

#Task 6
print("Average salary ==> : \n",data["salary"].mean())
print("Highest salary ==> : \n",data.sort_values("salary",ascending=False).head(1))
print("Lowest  salary ==> : \n",data.sort_values("salary",ascending=False).tail(1))
#Task 7

AI =data[data["department"]=="AI"]
print("AI department average salary : \n",AI["salary"].mean())
print("IT department average salary : \n",data[data["department"]=="IT"]["salary"].mean())

#Task 8
print("Employees with more then 4.5 rating :\n",data[data["rating"]>4.5])

#Task 9
print("correlation between salllary , experience , rating :\n",data[["salary","experience","rating"]].corr())

#Task 10

plt.plot(data["experience"],data["salary"],linestyle="--",color="g")
plt.xlabel("experience")
plt.ylabel("salary")
plt.title("experience VS salary")
plt.show()

plt.scatter(data["experience"],data["salary"],color="g")
plt.xlabel("experience")
plt.ylabel("salary")
plt.title("experience VS salary")
plt.show()

plt.bar(data["experience"],data["salary"],linestyle="--",color="b")
plt.xlabel("experience")
plt.ylabel("salary")
plt.title("experience VS salary")
plt.show()

#Task 11
H = data.groupby("department")["rating"].mean()
print(H.max())