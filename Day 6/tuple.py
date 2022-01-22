#data="sunil", "roshan",29
#for i in data:
#    print(i)
    
#python tuple slicing and indexing
data="sunil", "roshan",29
print(data[1])

#creating tuple using range() function
data= tuple(range(2,20,2))
print(data)

#python tuple len()
data="sunil", "roshan",29,0,4,"jhorley"
print(len(data))

#tuple with one element
a=(1)
b=(1,)
print(type(a))
print(type(b))

#python list inside tuple
data=(2,3,"name",["jhorley",46],{34,"sam"})
print(len(data))
#data[3].pop()
#print(data)
#data[3].append("Master")
#print(data)
data[4].remove("sam")
print(data)

#Python min and max function

print("maximum is:",max(1,2,34,35,23,67))
print("Minimum is:",min(1,2,34,35,23,67))

#Concatenation of two Tuple
#adding item in tuple
tuple1=("ram","shyam","mohan")
list1=list(tuple1)
list1.insert(3,"jhorley")
tuple2=tuple(list1)
print(type(tuple2))