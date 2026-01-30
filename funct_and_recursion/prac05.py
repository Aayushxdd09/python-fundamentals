def rem(l, word):
    n=[]
    for item in l:
        if item != word:
            n.append(item.strip(word))  #strip removes from starting and ending and  not middle
    return n

l = ["Harrany", "Shubhan", "Rahul", "an"]
a= (rem(l, "an"))
print(a)