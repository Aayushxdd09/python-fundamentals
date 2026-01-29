def greatest():
    a = int(input("Enter a num: "))

    b = int(input("Enter a num: "))

    c = int(input("Enter a num: "))

    if a>b and a>c:
        print(a)
        return a 
    
    elif b>c and b>a:
        print(b)
        return b

    elif c>a and c>b:
        print(c)
        return c
    
g1 = greatest()
print(g1)


    
