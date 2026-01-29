n = int(input("Enter a num: "))

i = 0

for i in range(0, n+1):
    print("*"*(n-i), end="")
    print(" "*i)
    i+=1
    if i==n:
        break
    