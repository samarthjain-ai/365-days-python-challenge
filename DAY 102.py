# DAY 102

import random

def play_round(max_range, attempts):

    number = random.randint(1, max_range)
    attempt = 0

    while attempt < attempts:
        try:
            guess = int(input("Enter your number here =>\n"))
        except:
            print("Invalid input")
            continue

        attempt += 1

        if guess > number:
            print("Too High")
        elif guess < number:
            print("Too Low")
        else:
            print("Correct 🎉")
            print(f"You guessed in {attempt} attempts")
            return

    print("GAME OVER ❌")
    print("Number was", number)


while True:
    print("Difficulty level - easy / medium / hard")

    difficulty = input("Choose difficulty level:\n").lower()

    if difficulty == "easy":
        play_round(50, 10)
    elif difficulty == "medium":
        play_round(100, 7)
    elif difficulty == "hard":
        play_round(200, 5)
    else:
        print("Invalid")
        continue

    again = input("Play again? (yes/no): ").lower()

    if again == "no":
        break