n1 = int(input("Enter first number "))
n2 = int(input("Enter second number "))
n3 = int(input("Enter third number "))
n4 = int(input("Enter fourth number "))

if (n1>n2 and n1>n3 and n1>n4):
    print(f"{n1} greatest ")

elif(n2>n1 and n2>n3 and n2>n4):
    print(f"{n2} is greatest")

elif(n3>n1 and n3>n2 and  n3>n4):
    print(f"{n3} is  greatest")

elif(n4>n1 and n4>n2  and n4>n3):
    print(f"{n4} is greatest")