words = ["donkey", "bad", "shit"]
with open("file_handling/prac05.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))


with open("file_handling/prac05.txt", "w") as f:
    f.write(content)
 