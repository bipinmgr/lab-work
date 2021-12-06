a=int(input("enter number to find sum of digits"))
sum=0
while (a>0):
    sum=sum+a%10
    a=a//10
print("Sum of digita is ",sum)