# Exam Performance Analyzer Pro
import numpy as np

Student_data=np.random.randint(30,100,size=(20,5))
print(f"===== Marks of 20 students in 5 subjects ===== \n{Student_data}")

print(f"Highest mark in the entire class \n {np.max(Student_data)}")
print(f"Lowest mark in the entire class  \n{np.min(Student_data)}")
print(f"Average mark of the class \n {np.mean(Student_data)}")
print(f"Total marks of the class  \n {np.sum(Student_data)}")


Total_marks=np.sum(Student_data,axis=1)
Avarage_marks=np.mean(Student_data,axis=1)
for i in range(len(Student_data)):
    print(f"Student {i+1} Total Marks : {Total_marks[i]}   and   Avarage Marks : {Avarage_marks[i]}")

print(f"Topper Marks student Id is  --> student {np.argmax(Total_marks)+1}") 
print(f"Topper Marks is  {np.max(Total_marks)}")
print(f"Lowest Marks student Id is  --> student {np.argmin(Total_marks)+1}")
print(f"Lowest Marks is  {np.min(Total_marks)}")

Avarage_subject_marks=np.mean(Student_data,axis=0)
for i in range(5):
    print(f"subject {i+1} Avarage is {Avarage_subject_marks[i]}")

print(f"Highest scoring subject ID  is --> subject {np.argmax(Avarage_subject_marks)+1} with avarage of {Avarage_subject_marks[np.argmax(Avarage_subject_marks)]}")
print(f"Lowest  scoring subject ID  is --> subject {np.argmin(Avarage_subject_marks)+1} with avarage of {Avarage_subject_marks[np.argmin(Avarage_subject_marks)]}")

Pass_student=0
Fail_student=0
Fail_student_id=[]
for id,i in enumerate(Avarage_marks):
    if i >=40:
        Pass_student+=1
    else:
        Fail_student_id.append(id)
        Fail_student+=1

print(f"Number of pass student is {Pass_student}")
print(f"number of fail student is {Fail_student} ")
print(f"Pass percentage {Pass_student*100/len(Student_data)}%")

for k in Fail_student_id:
    print(f"Fail student id are -> student {k+1}")


for id , avg in enumerate(Avarage_marks):
    if avg>=90:
         print(f"Student {id+1} -> Grade A")
    elif avg>=70:
        print(f"Student {id+1} -> Grade B")
    elif avg>=60:
        print(f"Student {id+1} -> Grade C")
    elif avg>=40:
        print(f"Student {id+1} -> Grade D")
    else:
        print(f"Student {id+1} -> Grade F")

print(np.argsort(Avarage_marks)+1)
i=1
for sort_avg in (np.argsort(Avarage_marks)[::-1]):
    
    print(f"Rank {i} - student {sort_avg+1} avarage marks {Avarage_marks[sort_avg]}")
    i+=1


print(f"Student with the avarage more then 80 ")
for id, avg in enumerate(Avarage_marks):
    if avg >80:
        print(f" student {id+1} - {avg}")


print(f" Students with the avarage less than 50 ")
for id, avg in enumerate(Avarage_marks):
    if avg <50:
        print(f" student {id+1} - {avg}")

greater_90=0
greater_80=0
mid_40_79=0
less_40=0

for i in Student_data:
    for j in i:
        if j >=90:
            greater_90+=1
        elif j>=80:
            greater_80+=1
        elif j<40:
            less_40+=1
        else:
            mid_40_79+=1


print(f"student with marks greater then 90 are {greater_90}")
print(f"student with marks greater then 80 are {greater_80}")
print(f"student with marks less    then 40 are {less_40}")
print(f"student with marks greater then 40 and less then 80 are {mid_40_79}")



print(f"========= FINAL REPORT =========")
print(f"Class Avarage is {np.mean(Student_data)}")
print(f"Topper  is       : student {np.argmax(Avarage_marks)+1}")
print(f"Topper Marks     : {np.sum(Student_data[np.argmax(Total_marks)])}")
print(f"Lowest Performer : student{np.argmin(Avarage_marks)+1}")
print(f"Pass Percentage  : {Pass_student*100/len(Student_data)}%")
print(f"Best Subject     : {np.argmax(Avarage_subject_marks)+1}")
print(f"Worst Subject    : {np.argmin(Avarage_subject_marks)+1}")
