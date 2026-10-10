def vowels_count(sentence):
    vowels = 0
    for i in sentence:
        if i.lower() in "aeiou":  
            vowels += 1
    return vowels

print(vowels_count("asdjhagsdasjghdfaskjdgasgdasdgsjhdsjhdsjdhsjdhsjdhsdhsjhjs"))
