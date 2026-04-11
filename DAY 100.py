#DAY 100 

import random 

user_name = input("Enter your name ")
number = random.randint(1,100)
attempts = 0

print(f"Welcome {user_name}, Guess the number between 1 to 100")
print("You have onlr 5 chances")

while True:

    guess = int(input("Enter you value\n"))
    attempts+=1
    if attempts <=5:
        print("Attempts ==> ",attempts)

        if guess > number:
            print("Too High\n")
            attempts+=1
        elif guess < number:
            print("Too Low\n")
            attempts+=1
        else:

            print("Correct\n")
            attempts+=1
            print(f"{user_name}, you guess it in {attempts} attempts ")
            break
    else:
        print("Attempts End")
        print("Game over\n")
        print(f"The correct number was {number}")
        break

