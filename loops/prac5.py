n = int(input("Enter a number: "))

sum = 0
i = 0

while(i<=n):
    sum += i
    i+=1

print(sum)


#WITH FOR LOOP

sum = 0
for i in range(0, n+1):
    sum+=i
    #i+=1

print(sum)