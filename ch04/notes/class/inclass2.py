# def foo(param1,param2):
#     return param1+param2

# def bar(param1=4, param2=3):
#     if True:
#         return param1+param2
#     else:
#         pass

# #foo(1,2)
# # bar(1)
# # bar()
# # bar(1,3)

# result=bar(param2=1,param1=2)
# print(result)

def percenttoletter(percent):
    let="A"
    if percent < 90:
        let="B"
    elif percent < 80:
        let="C"
    elif percent < 70:
        let="D"
    else:
        let="D"
    return let

def percenttoletter(percent):
    letter="A"
    return letter
def ispassing(letter):
    passing=True
    return passing 
def main():
    let=percenttoletter(90)
    if ispassing(let):
        print("you passed")
    else:
        print("someone messed up your grades")