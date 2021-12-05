#A school decided to replace the desk in three classrooms, Each desk sits two students
#Given the number of students in each class,
#print the smallest possible number of desks that can be purchased.
#The program should read three integers:The number of student in each of the three
#Class a,b and c respectively.
#Suppose in the first test there are three groups. The first group has 20 and thus needs 10 desks.'
#The second group has 21 students, so they can get by with no fewer than 11 desks.
#11 desks are also enough for the third group of 22 students. So, we need 32 desks in total.

x=int(input("Enter the number of sutdent in first class"))
y=int(input("Enter the number o fstudent in second class"))
z=int(input("Enter the number of student in third class"))
sum=x//2+y//2+z//2+x%2+y%2+z%2
print(f"Total number of bench we need {sum}")
