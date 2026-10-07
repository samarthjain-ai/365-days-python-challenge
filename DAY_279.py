def hollow_diamond(n):

    for i in range(n):
        spaces = " " * (n - i - 1)

        if i == 0:
            print(spaces + "*")
        else:
            inside_spaces = " " * (2 * i - 1)
            print(spaces + "*" + inside_spaces + "*")

    for i in range(n - 2, -1, -1):
        spaces = " " * (n - i - 1)

        if i == 0:
            print(spaces + "*")
        else:
            inside_spaces = " " * (2 * i - 1)
            print(spaces + "*" + inside_spaces + "*")

hollow_diamond(5)