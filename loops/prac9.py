n= int(input("Enter a num: "))


i = 0

for i in range(1, n+1):
    if(i%2==0):
        print("* "*2)

    else:
        print("*"*n)