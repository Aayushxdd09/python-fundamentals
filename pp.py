class CoffeeMachine:
    def __init__(self):
        self._water = 100      # 🔒 Encapsulation (protected data)
        self._beans = 50

    # ⭐ Abstraction — simple public method
    def make_coffee(self):
        if self._water >= 20 and self._beans >= 10:
            self._heat_water()
            self._grind_beans()
            self._brew()
            print("Coffee ready ☕")
        else:
            print("Not enough resources")

    # 🔒 Internal methods (hidden details)
    def _heat_water(self):
        self._water -= 20

    def _grind_beans(self):
        self._beans -= 10

    def _brew(self):
        pass  

machine = CoffeeMachine()
machine.make_coffee()
machine.make_coffee()
machine.make_coffee()
machine.make_coffee()
machine.make_coffee()
machine.make_coffee()
machine.make_coffee()
