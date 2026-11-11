n = int(input("enter a number  here  number here : "))

for i in range(1, n + 1):
    stars = "*" * i
    spaces = " " * (2 * (n - i))
    print(stars + spaces + stars)


for i in range(n - 1, 0, -1):
    stars = "*" * i
    spaces = " " * (2 * (n - i))
    print(stars + spaces + stars)