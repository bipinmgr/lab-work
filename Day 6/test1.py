#data=["sunil","roshan",'34']
#for i in data:
#    print(i)

#data=list(range(0,10,2))
#for i in data:
#    print(i)

#data=["a","b","c","d","4"]
#print(data)
#data.append(9)
#data.append("programming")
#print(data)

#data=["a","b","c","d","4"]
#print(data)
#data.insert(-2,"Inserted")
#print(data)

#inserting a tuple(as an element) to the list

#mixed=[{1,2},[5,6,7],{"a":"r"}]
#ntuple=(4,5)
#mixed.insert(2,ntuple)
#print(mixed)

#updating elements in the list
data=["a","b","c",9]
print(data)
data[0]="jhorley"
data[1]="islove"
data[2]=23
print(data)

#python list del function
data=["a","b","c",9]
print(data)
del data[2]
print(data)

#python list remove
data=["a","b","c",9]
print(data)
data.remove("c")
print(data)

#python list pop
data=["a","b","c",9]
print(data)
data.pop()
print(data)

#Concatenationn of two lists
data=["a","b","c",9]
data2=[9,4,7]
print(data+data2)

#python list copy
data=["a","b","c",9]
data2=["hawa"]
data2=data.copy()
print(data)
print(data2)

#python list extend
data=["a","b","c",9]
data2=["hawa"]
data2.extend(data)
print(data2)

#Python list clear

data=["a","b","c",9]
data.clear()
print(data)
