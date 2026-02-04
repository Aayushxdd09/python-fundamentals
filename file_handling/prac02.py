import random

def game():
    score = random.randint(1, 100)
    print("You are playing the game")
    print(f"Your score is {score}")
    return score

yourscore = game()
number = ""
with open("file_handling/prac02high_score.txt") as f:
    content = f.read()
   # print(content)
    for char in content:
        if char.isdigit():
            
            number+=char

if number == "":
    number = 0
else:
    number = int(number)

print(f"Previous high score = {number}")

if(yourscore>number):

    with open("file_handling/prac02high_score.txt", "w") as g:
        g.write(f"high score = {yourscore}")
        print("New High score is", yourscore)
    
else:
    print("High score remains the same", number)
