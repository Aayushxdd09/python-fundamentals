'''We dont have to  really assign name and  language variablles 
 again and again differently(like: n1, n11, n2) but if the  same keys
 appears it will take the latest one but it can take muultiple same 
 values. there cant be 2 ayush but pythhon can be language of onne or
 more people'''



s = {}

n1 = input("Enter your name: ")
n11 = input(f"Enter the {n1}'s language  name: ")
s.update({n1:n11})
n2 = input("Enter your name: ")
n22 = input("Enter the language  name: ")
s.update({n2:n22})
n3= input("Enter your name: ")
n33 = input("Enter the language  name: ")
s.update({n3:n33})
n4= input("Enter your name: ")
n44 = input("Enter the language  name: ")
s.update({n4:n44})

print(s)
print(type(s))