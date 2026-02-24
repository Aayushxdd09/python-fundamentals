class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)   # initializes brand from parent
        self.model = model        

    def show(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

c = Car("Toyota", "Fortuner")
c.show()
