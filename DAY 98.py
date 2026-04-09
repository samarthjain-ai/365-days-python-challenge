# DAY 98
# Q1 - even odd
def even_odd(n):
    if n%2==0:
        return "Even"
    else:
        return "Odd"

result = even_odd(345)
print(result)

#Q2 - sum of list
def list_sum(*args):
    total=0
    for num in args:
        total +=num

    return total
result = list_sum(1,2,3,4)
print(result)

#Q3 - Minimun Number

def smallest(*args):
    smallest=args[0]
    for num in args:
        if num < smallest:
            smallest = num

    return smallest

result = smallest(12,2,3,2,1,2,33,44,6)
print(result)

#Q4 - count words

def count_words(sentence):
    words = sentence.split()
    return len(words)

result= count_words("I love Python")
print(result)

