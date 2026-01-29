num = int(input("Enter your number: "))

if (num%2 == 1):

    print("Odd")
else:
    print("Even")

age = int(input("Enter your age: "))

if (age>=18 and age<=100):
    print("Youre an adult")

elif (age<0):
    print("Enter a valid age number")

elif (age>100):
    print("Too old")

else:
    print("Youre not an adult")


