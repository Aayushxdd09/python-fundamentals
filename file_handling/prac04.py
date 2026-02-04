
with open("file_handling/prac04.txt", "r") as f:
    content = f.read()


content = content.replace("journey", "experience")


with open("file_handling/prac04.txt", "w") as f:
    f.write(content)
