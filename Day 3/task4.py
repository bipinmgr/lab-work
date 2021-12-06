#Given three integers, print the smallest one
#(Three integers should be user input)
a=int(input("Enter first integer"))
b=int(input("enter second integer"))
c=int(input("Enter third integer"))

if a<=b and a<=c:
    print("a is smaller among b and c")
elif b<=a and b<=c:
    print("b is smaller among a and c")
else:
    print(" is smaller among b and a")
