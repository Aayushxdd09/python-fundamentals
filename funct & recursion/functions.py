def avg():  #FUNCTION DEFINITION

    a = int(input("Enter the first num: "))

    b = int(input("Enter the second num: "))

    c = int(input("Enter the third num: "))

    average = (a + b + c)/3
    print(average)
    return average  #EXECUTES ONLY WHEN THERES A VARIABLE

a  =  avg() #FUNCTION CALL
print("Average is= ", a)


b = avg()
print("Average is= ", b)

c =  avg()
print("Average is = ", c)

avg()