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
    
    diff = abs(computer - usernum)

    if diff <= 5:
        if usernum < computer:
            print("A bit higher")
        else:
            print("A bit lower")
    elif usernum < computer:
        print("Too low")
    else:
        print("Too high")