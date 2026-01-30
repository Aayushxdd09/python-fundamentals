password = input("Enter your password: ")

if(len(password) < 8):
    print("Password lenght too short")
    print("Try again")
    exit()

else:
    numbers = {"1","2", "3", "4", "5", "6", "7", "8", "9","0"}
    spec_char = {"!", "@", "#", "%", "^", "&", "$", "*"}

    has_num = 0
    has_schar = 0

    for char in numbers:
        if char in password:
            has_num +=1

        
    for schar in spec_char:
        if schar in password:
            has_schar +=1

if (has_num == 0 and has_schar == 0):
    print("Weak password")
    

elif (has_num >= 1 and has_schar == 0):
    print("Medium strenght Password")
                       
elif (has_num == 0 and has_schar >= 1):
    print("Medium strenght Password")

elif (has_num >= 1 and has_schar >= 1):
    print("strong strenght Password")


                       


             
