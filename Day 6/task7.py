#Write a Python program to multiply all the numbers in a list.
#Sample list = [8,2,3,-1,7]

#multiply all values in list usiing traversal

def mult(list):
    #multiply elements one by one
    result=1
    for x in list:
        result=result*x
    return result
    #driver code
mylist=[8,2,3,-1,7]
print(mult(mylist))