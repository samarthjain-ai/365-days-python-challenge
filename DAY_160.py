def analyze(marks):

    print("Highest marks ==> ",max(marks))
    print("Lowest  marks ==> ",min(marks))
    print("Avarage marks ==> ",sum(marks)/len(marks))
    pass_count=0
    fail_count=0

    for mark in marks:
        if mark >=40:
            pass_count+=1
        else:
            fail_count+=1
    
    print("Pass Count ==> ",pass_count)
    print("Fail count ==> ",fail_count)

marks = [78, 45, 90, 67, 34, 88, 56]
analyze(marks)

name = "Samarth Jain"
count=0

print("Name in uppercase ==> ",name.upper())
print("Name in lowercase ==> ",name.lower())
print("Reverse the name ==> ",name[::-1])

vowle_count=0
constant_count=0
for i in name:
    if i in "AEIOUaeiou":
        vowle_count += 1
    elif i != " ":
        constant_count += 1
print("Vowel count ==> ",vowle_count)
print("Constant count ==> ",constant_count)