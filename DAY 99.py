#DAY 99
#Q1 - Palindeome Check

def check_palindeome(n):
    s = str(n)
    if s==s[::-1]:
        return True
    else :
        return False
result = check_palindeome(121)
print(result)

#Q2 - Factorial 

def check_factorial(n):
    fact = 1
    for i in range(2,n+1):
        fact = fact*i
        

    return fact
result = check_factorial(6)
print(result)

#Q3 -count upper and lower case

def count_up_lower(sentance):
    upper_count = 0
    lower_count=0
    upper = "ABCDEFGHIJKLMONPQRSTUVWXYZ"
    for i in sentance:
        if i.isupper():
            upper_count+=1
        elif i.islower():
            lower_count+=1

    return upper_count ,lower_count
result  = count_up_lower("I LOve Python")
print(result)

#Q4 - Find the second largest number
def second_largest(*args):
     largest = second = float("-inf")
     for num in args:
         if num> largest:
                second =largest
                largest=num
         elif num > second and num != largest:
             second =num

     return second
result = second_largest(1,2,3,9,4,3,33,4,44,49,4)
print(result)