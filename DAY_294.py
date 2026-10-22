rows = int(input("Enter a number here "))

for i in range(1, rows + 1):
    spaces = rows - i
    stars = 2 * i - 1

    print(" " * spaces + "*" * stars)