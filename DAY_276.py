def number_pyramid(n):
    for i in range(n):
        spaces = " " * (n - i - 1)
        numbers = "".join(str(j) for j in range(1, 2 * i + 2))
        print(spaces + numbers)

number_pyramid(5)