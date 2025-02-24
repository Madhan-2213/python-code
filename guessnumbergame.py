import random

num = random.randint(1, 20)
guess = int(input("Guess a number between 1 and 20: "))
attempt = 1
while num != guess:

        if num < guess:  #12  13
            print("Too high")
        else:
            print("Too low")
        guess = int(input("Guess a number between 1 and 20: "))
        attempt += 1
        if attempt == 4:
             print("You lost")
             break

else:
    print("You guessed correctly")
