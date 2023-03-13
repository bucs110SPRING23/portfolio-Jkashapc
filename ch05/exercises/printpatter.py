def starpyr(rows):
    for i in range(1,rows + 1):
        print("*"*i)

def rstarpyr(rows):
    for i in range (rows, 0, -1):
        print("*"*i)

levels=int(input("what height do you want your pyramid to be?:"))
starpyr(levels)
rstarpyr(levels)