def palindrome_pyramid(n):
    for i in range(n):
        spaces = " " * (n - i - 1)

        increasing = "".join(str(j) for j in range(1, i + 2))
        decreasing = "".join(str(j) for j in range(i, 0, -1))

        print(spaces + increasing + decreasing)


palindrome_pyramid(5)