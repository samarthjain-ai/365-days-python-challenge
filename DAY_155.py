def student_result(marks):

    if marks >= 90:
        return "A"

    elif marks >= 75:
        return "B"

    elif marks >= 60:
        return "C"

    elif marks >= 35:
        return "D"

    else:
        return "FAIL"


try:
    marks = int(input("Enter your marks here: "))

    result = student_result(marks)

    print("Grade =", result)

except ValueError:
    print("Enter a valid input PLZ")