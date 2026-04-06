# DAY 95 
#Q1 count words 

sentence= input("Enter your sentance here ==> \n")
words= sentence.split()
print(len(words))

#Q2 second largest number

numbers = [10,2,34,56,90,99]
largest = float('-inf')
second_largest = float('-inf')

for num in numbers:
    if num>largest:
        second_largest = largest
        largest=num
    elif num> second_largest and num != largest:
        second_largest = num
print("Second largest => ",second_largest) 

#Q3 remove space from string 

sentence_2= input("Enter your sentence here ==>\n")
words_2= sentence_2.split()
result = "".join(words_2)
print(result)