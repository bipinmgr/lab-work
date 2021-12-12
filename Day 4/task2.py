#Write a Python program to sum three given integers. However, if two or more values are
#equal sum will be zero

a=int(input("Enter any integer number"))
b=int(input("enter any integer number"))
c=int(input("enter any integer number"))

sum=a+b+c


if (a==b==c) or (b==c==a) or (c==b==a):
    print("The sum is 0")
else:
    print(f"sum of given integers is {sum}")

