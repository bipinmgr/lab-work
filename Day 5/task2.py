#Write a python program to guess a number between 1 to 9

#for i in range(0,10):
#    print("Guess any number")
#    number=int(input("Guess any number"))
#    if int(number)==range(0,10):
#        print("Well guessed")
#else:
#    print("5 attempt finished")
import random
target_num, guess_num = random.randint(1,10),0
while target_num != guess_num:
    guess_num=int(input("Guess a number between 1 and 10 "))
    print("Well guessed ! ")