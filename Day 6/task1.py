#Write a Python program to reverse a string.

def reverse(str):
    s=""
    for i in str:
        s=i+s
    return s
string="Jhorley"
print("GIVEN STRING:", string)
print("Reversed string:",reverse(string))