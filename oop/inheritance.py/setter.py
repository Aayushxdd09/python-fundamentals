class Employee:
    a = 1

    @classmethod   
    def show(cls):
        print(f"Class attribute is {cls.a}")

    @property  #turns a method into something that behaves like a variable
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self, value):
        first, last = value.split()
        self.fname = first
        self.lname = last
        

e = Employee()
e.a = 45

e.name ="Harry Khan"
print(e.name)
print(e.fname, e.lname)
e.show()
