word = "donkey"
with open("file_handling/prac05.txt", "r") as f:
    content = f.read()


content = content.replace(word, "######")


with open("file_handling/prac05.txt", "w") as f:
    f.write(content)
