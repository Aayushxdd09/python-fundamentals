import random
random_num = random.choice([-1, 0, 1])

computer = random_num

youstr = input("Enter your choice btw s, w or g: ")
youdict={"s": 1, "w": -1, "g":0}
reversedict= {1: "snake", -1:"water", 0:"gun"}

you = youdict[youstr]

print(f"You chose {reversedict[you]}    \nComputer chose {reversedict[computer]}")

if(computer==you):
    print("Its a draw")
else:
    if (computer == -1 and you == 1):
        print("You Win!")
    elif (computer == -1 and you == 0):
        print("You lose!")

    elif (computer == 1 and you == -1):
        print("You lose!")
    elif (computer == 1 and you == 0):
        print("You Win!")

    elif (computer == 0 and you == -1):
        print("You win!")
    elif (computer == 0 and you == 1):
        print("You lose!")

    else:
        print("Something went wrong")