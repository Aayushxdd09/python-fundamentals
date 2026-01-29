p1 = "make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "Click this "

p5 = [12, 34, 65, "object values"]

message = input("Enter your string ")
if p1 in message or p2 in message or p3 in message or p4 in message:
    print("spam!!!")

else:
    print("Not spam")

