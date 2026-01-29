def greet(name, ending):
    print("Good Day, " + name)
    print(ending)
    return "It's Done"   #IF NOT USED, IT WILLL SHOW "NONE" FOR VARIABLES

a = greet("Harry", "Zhank ouy")
print(a)   #THERE NOTHING ACTUALLY COMING IN THIS VARIABLE IF WEE SEE THE
           #PROGRAM SO WE PUT RETURN IN DEF FUNCTION SO THAT THIS VARIABLE
           #WILL TAKE THAT VALUE AND RETURN THAT
           
b = greet("Arshad", "Thanks")
print(b)   

print(a) #NOW THE RETURN  VALUE "DONE"  IS STORED IN VARIABLES


c = greet("Manav", "Thank you")


greet("Aryan", "Thank you so much")

print(b)
print(c)
print(a)