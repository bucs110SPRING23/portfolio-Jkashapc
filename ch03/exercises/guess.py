import random 
num=random.randrange(1,10)
guess=int(input("Guess the number we are thinking:"))
while num!=guess:
    if guess > num:
        print("Too high bozo")
        guess=int(input("Guess the number again you bum:"))
    elif guess < num:
        print("Too low idiot!")
        guess=int(input("last chance to guess:"))
    else:
        break
    print("You got it!")