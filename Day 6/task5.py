#5. Write a program function to find min of three numbers.(no parameter and no return type)

a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))

def f():
    if a<b & a<c:
        print("min number is a")
    elif b<a & b<c:
        print("min number is b")
    else:
        print("min number is c")
f()