#write a python program that accepts a string and calculate the number of digits and letters=input("INput a string")

s=input("Enter a string")
d=l=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("Letters",l)
print("Digits",d)