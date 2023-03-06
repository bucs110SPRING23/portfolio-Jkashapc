#vending machine 
#black boxing 

print("welcome to vending machine")
code=input("Please enter a code:")
money=input("give me money:")

def myvendingmachine():
    if code == "A":
        if money >= 1:
            print("you got coke")
        else:
            print("more money please")
    elif code == "B":
        if money>=1.5:
            print("you got water")
        else:
            print("more $")
    else:
        print("invalid code or $")

myvendingmachine()


#functions are always defined in global scope 
#scope-where the data/algorithim is accesible