import random 
num=random.randrange(1,1000)
guess=int(input("Guess the number we are thinking:"))
count=0
for i in range(1000):
    if guess > num:
        print("Too high bozo")
        guess=int(input("Guess the number again you bum:"))
        count += 1
    elif guess < num:
        print("Too low idiot!")
        guess=int(input("Try again idiot:"))
        count +=1
    else:
        print("You got it in", str(count),"tries!")
        break
