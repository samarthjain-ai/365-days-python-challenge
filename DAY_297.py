rows = int(input("Enter the number of rows for the upper half: "))

for i in range(1, rows + 1):
    spaces = rows - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)


for i in range(rows - 1, 0, -1):
    spaces = rows - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)
