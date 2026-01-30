import random

computer = random.randint(1,100) 

attempts = 0
while True:
    usernum = int(input("Enter a number: "))
    attempts +=1
    if(computer == usernum):
        print("You guessed it right! ")
        print(f"Total attempts taken = {attempts}")
        break
    elif(computer>usernum):
        print("Too low")
        
    elif(computer<usernum):
        print("Too high")
       
