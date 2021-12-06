#WAP which accepts marks of four subjects and display total marks, percentage
#and grade. 
# #HINT: more than 70%- Distinction, more than 60%-first,
# more than 40%-pass, less than 40%- fail

a=int(input("Enter obtained marks in Math"))
b=int(input("Enter obtained marks in Biology"))
c=int(input("Enter obtained marks in Chemistry"))
d=int(input("Enter obtained marks in physic"))

#t=total marks
t=a+b+c+d
print(f"Total marks obtained in all sub {t}")

#p=percentage
p=(t/400)*100
print(f"Total percentage Obtaine {p}")

if p>70:
    print("Distinction")
elif p>=60:
    print("First Division")
elif p>=40:
    print("Pass")
else:
    print("Fail")