#Write a program that asks the user for a number in the range of 1 to 12. 
# The program should display the corresponding month, where 
#1=january, 2=february,3=march,4=april,5=may,6=june,7=july, 8=august,
# 9=september,10=october,11=november,12=december. The program should
#  display an error message if the user enters a number
#that is outside the range of 1 to 12

a=int(input("Enter any number from 1-12"))

if a==1:
    print("Jan")
elif a==2:
    print("Feb")
elif a==3:
    print("Mar")
elif a==4:
    print("april")
elif a==5:
    print("may")
elif a==6:
    print("june")
elif a==7:
    print("july")
elif a==8:
    print("august")
elif a==9:
    print("sept")
elif a==10:
    print("oct")
elif a==11:
    print("nov")
elif a==12:
    print("dec")
else:
    print("You are out of range")