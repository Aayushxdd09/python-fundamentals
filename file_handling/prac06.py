with open("file_handling/prac06log.txt") as f:
    lines = f.readlines()

linenum = 1
for line in lines:
    if("python" in line):
        print(f"yes python is present in line {linenum}")
        break 
    linenum+=1
else:
    print("No python is not present")

print(lines)