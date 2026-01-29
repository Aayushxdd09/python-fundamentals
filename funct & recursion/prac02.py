def converter():
    
    c = int(input("Enter the temp in celcius: "))

    f =  (c*9/5) + 32

    print(f"Temp in Farhenite is {f}f")
    return f

a = converter()
print(a)