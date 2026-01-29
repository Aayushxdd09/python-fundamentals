num = int(input("Enter a number: "))

for i in range(1, 11):
    i = i*num
    print(i)
    i+=1
    
for i in range(1,11):
    print(f"{num} X {i} = {i*num}")

