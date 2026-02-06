with open("file_handling/prac05.txt") as f:
    content = f.read()

with open("file_handling/prac07copy.txt", "w") as f:
    f.write(content)