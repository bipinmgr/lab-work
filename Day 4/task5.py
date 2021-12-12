
#a student will not be allowed to sit in exam if his/her attendence is less than 75%:
#Take following input from user 
#Number of classes held
#Number of classes attended
#and print percentage of class attended
#Is student is allowed to sit in exam or not

a=int(input("Enter no of classes held:"))
b=int(input("Enter no of classes attended:"))
percentage=(b/a)*100
if percentage<=75:
    print("He/she will not be allowed to sit in exam")
elif percentage>75:
    print("He/she is allowed to sit in exam")