def first_unique_char(text):
    for char in text:
        if text.count(char) == 1:
            return char

    return "No unique character found"


print(first_unique_char("aabbcddee"))
print(first_unique_char("aabb"))