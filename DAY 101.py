#DAY 101 
# Guessing game update
import random
play_game="yes"

while play_game=="yes":

    print("Welcome to Gressing game")
    print("-----Levels-----")
    print("easy = attempts -10 in between 1 t0 50")
    print("medium = attempts -7 in between 1 t0 100")
    print("hard = attempts -5 in between 1 t0 200")

    play_game =input("Play again (yes/no)\n").lower()
    if play_game=="no":
        break
    difficulty  = input("Difficulty level - easy/medium/hard\n").lower()

    if difficulty == "easy":
        numbers=random.randint(1,50)
        attempts =0
        try:
            
            while attempts<10:
                guess=int(input("Enter your number ==>\n"))
                if guess > numbers:
                    print("Too High")
                    attempts+=1
                elif guess < numbers:
                    print("Too Low")
                    attempts+=1
                else:
                    print("Correct you win ")
                    print(f"You guess in {attempts} attempts")
                    break
            else:
                print("Try againe\n")
                print("Number was ==> ",numbers)
        except :
            print("Invalid input")
            continue

    if difficulty == "medium":
        numbers=random.randint(1,100)
        attempts =0
        try:
            
            while attempts<7:
                guess=int(input("Enter your number ==>\n"))
                if guess > numbers:
                    print("Too High")
                    attempts+=1
                elif guess < numbers:
                    print("Too Low")
                    attempts+=1
                else:
                    print("Correct you win ")
                    print(f"You guess in {attempts} attempts")
                    break
            else:
                print("Try againe\n")
                print("Number was ==> ",numbers)
        except :
            print("Invalid input")
            continue

    if difficulty == "hard":
        numbers=random.randint(1,200)
        attempts =0
        try:
            
            while attempts<5:
                guess=int(input("Enter your number ==>\n"))
                if guess > numbers:
                    print("Too High")
                    attempts+=1
                elif guess < numbers:
                    print("Too Low")
                    attempts+=1
                else:
                    print("Correct you win ")
                    print(f"You guess in {attempts} attempts")
                    break

            else:
                print("Try againe\n")
                print("Number was ==> ",numbers)
        except :
            print("Invalid input")
            continue




