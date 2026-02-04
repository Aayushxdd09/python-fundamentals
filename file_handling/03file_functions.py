f = open("file_handling/file_read.txt")

#lines = f.readlines()
#print(lines)
#print(type(lines))  #It retrns as a list
'''
line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

line3 = f.readline()
print(line3)

line4 = f.readline()
print(line4 == "") #it wont show anything as we dont have line 4 in the txt file
'''
line = f.readline()
while(line!=""):
    print(line)
    line=f.readline()

f.close()
