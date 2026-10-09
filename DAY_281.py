def count_characters(text):
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

result_hello = count_characters("hello")
for char, count in result_hello.items():
    print(f"{char}: {count}")

print() 

result_python = count_characters("python")
for char, count in result_python.items():
    print(f"{char}: {count}")
