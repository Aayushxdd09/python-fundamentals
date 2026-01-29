a = (1,)  # give comma for single entry in tuple else it would consider it as integer
print(type(a))
print(a)

b = input("Enter the name: ")
tup= (b,)
print(type(tup))
print(tup)

c = (1, 45, 342, 45, 3424, False, "Rohan")
no = c.count(45)   #counts the num of times it came
ind = c.index(3424)
print(no)
print(ind)

tuple_add = c + tup + a  #We can also add tuples
print(tuple_add)
print(len(tuple_add))

# slicing

d = (45, 56, 49, "harry", 32)
sliced = d[1:4]
print(sliced)