def first_non_repeating(text):

    frequency = {}

    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    for char in text:
        if frequency[char] == 1:
            return char

    return "No non-repeating character"


print(first_non_repeating("aabbcdeff"))
print(first_non_repeating("aabbcc"))
print(first_non_repeating("swiss"))
print(first_non_repeating("programming"))