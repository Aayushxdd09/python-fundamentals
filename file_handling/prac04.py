# Step 1: Read the file
with open("file_handling/prac04.txt", "r") as f:
    content = f.read()

# Step 2: Replace the word
content = content.replace("journey", "experience")

# Step 3: Write back to the same file
with open("file_handling/prac04.txt", "w") as f:
    f.write(content)
