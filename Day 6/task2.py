# Write a function called fizz_buzz that takes a number.
#If the number is divisible by 3, it should return “Fizz”.
#If it is divisible by 5, it should return “Buzz”.
#If it is divisible by both 3 and 5, it should return “FizzBuzz”.
#Otherwise, it should return the same number.

def fizzbuzz(number):
    if number % 3==0 & number %5==0:
        print("Fizzbuzz")
    elif number%3==0:
        print("Fizz")
    elif number%5==0:
        print("buzz")
    else:
        print("Number")