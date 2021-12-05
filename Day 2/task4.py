#N students take K apples and distrubute them among each other evenly. 
#The remaining (the indivisible)part remains in the basket.BaseExceptionHow many apples will each single student get?
#How many apples will remain in the basket?the program reads the numbers N and K.
#It shoulrd pront the two answers for the questions above.

N=int(input("enter the number of sutdents"))
A=int(input("enter the number of apples"))
x=A//N
y=A%N
print(f"Each student will get {x} apples")
print(f"Remainnig apples in the basket {y} ")