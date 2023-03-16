def exponent(x,y):
    number=1
    for _ in range(y):
        number =number*x
    return number 
def multiply(x,y):
    number=0
    for _ in range(y):
        number+number+x
    return number 
def square(x):
    return exponent (x,2)
def main():
    x=int(input("Choose number:"))
    y=int(input("Choose another:"))
    result=multiply(x,y)
    print(result)
    result=exponent(x,y)
    print(result)
    result=square(x)
    print(result)
