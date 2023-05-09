import random 
num=random.randrange(1,10)
guess=int(input("Guess the number we are thinking:"))
for i in range(3):
    if guess > num:
        print("Too high bozo")
        guess=int(input("Guess the number again you bum:"))
    elif guess < num:
        print("Too low idiot!")
        guess=int(input("last chance to guess:"))
    else:
        print("You got it!")
        break