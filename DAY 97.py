#DAY 97 
#Q1 -prime number

def is_prime(n):
    if n>1:
        return False
    
    for num in range(2,num):
        if n% num ==0:
            return True
    return True

if is_prime(7):
    print("IT IS PRIME")
else:
    print("NOT PRIME")

#Q2 -Reverse String

def reverse_string(sentence):
    rev = str(sentence[::-1])
    return rev
result = reverse_string("Hello")
print(result)

#Q3 - vowels 

def count_vowel(sentence):
    count_v=0
    for char in sentence:
        if char in "AEIOUaeiou":
            count_v+=1
    return count_v

result =count_vowel("samarth jain is my name")
print(result)