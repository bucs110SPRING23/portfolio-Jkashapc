n=int(input("how many rows of stars"))
def starpyr():
    for i in range(rows):
        for j in range(i+1):
            print("* ", end="")
        print("\n")

        