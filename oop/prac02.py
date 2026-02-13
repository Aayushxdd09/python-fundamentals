class Calculator():
    def __init__(self, num):
        self.num = num
        print(f"The  number is {num}")

    def square(self):
        print(f"The square is {self.num*self.num}")

    def cube(self):
        print(f"The cube is {self.num * self.num * self.num}")

    def squareroot(self):
        print(f"The square root is {self.num **(1/2)}")

    @staticmethod
    def greet():      
            print("Alright then:")


a = Calculator(4)
a.greet()
a.square()
a.cube()
a.squareroot()
