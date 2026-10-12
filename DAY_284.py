# Day_284.py

def are_anagrams(str1, str2):

    str1 = str1.lower()
    str2 = str2.lower()
    
    return sorted(str1) == sorted(str2)

print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("hello", "world"))    # False
