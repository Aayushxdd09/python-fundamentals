from random import randint

class Train:

    def __init__(self, trainNo):
           self.trainNo = trainNo


    def book(self, fro, to):
            print(f"Ticket is booked in Train number: {self.trainNo}. From {fro} to {to}")

    def getstatus(self):
            print(f"Train number: {self.trainNo} is running on time ")

    def getfare(self, fro, to):
            print(f"Ticket fare in Train number: {self.trainNo} from {fro} to {to} is {randint(222, 555)}")


t = Train(12399)
t.book("Rampur", "Delhi")
t.getstatus()
t.getfare("Rampur", "Delhi")