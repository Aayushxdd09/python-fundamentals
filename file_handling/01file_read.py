f  = open("file_handling/file_read.txt")  #By default its in read mode, for write mode- (, "w")

data = f.read()

print(data)

f.close()