logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""
import random
numbers = list(range(1, 101))
def guesser(diffi):
    num = random.choice(numbers)
    right = 0
    if diffi == "easy":
        diffi = 10
        print(f"You have {diffi} guesses")
    else:
        diffi = 5
        print(f"You have {diffi} guesses")

    for guesses in range(diffi):
        guessed_num = int(input("Enter a number between 1 and 100:  "))
        if guessed_num==num:
            right = 1
            print(f"You are right the number is {num}")
            break
        elif guessed_num>num:
            print("Too high")
            print(f"You have {diffi-guesses-1} guesses left")
        else :
            print("Too low")
            print(f"You have {diffi - guesses - 1} guesses left")
    if right!=1:
        print(f"You lost the number was {num}")


print(f"{logo}\nWelcome to the number guessing game!\nI'm thinking of a number between 1 and 100.")
diff = input("Choose a difficulty, type 'easy' or 'hard'  ")

guesser(diff)