class Programmer():

    company = "Microsoft"

    def __init__(self, name, salary, pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode

p = Programmer("Harry", 2000000, 400201)
print(p.name, p.salary, p.pincode, p.company)

r = Programmer("Rohan", 1800000, 300105)
print(r.name, r.salary, r.pincode, r.company)