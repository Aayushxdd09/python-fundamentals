list1= ["apple", "orange", 356, 89.094, "harry", False]
print(list1[0])

list1[0]= "green"
print(list1)

print(list1[0:3])  #slicing just like strings
list1.append("ayush")
list1.append(56)
list1.insert(3, 8)  #first index no. then value
print(list1)
list1.pop(0)
list1.remove("harry")
print(list1)