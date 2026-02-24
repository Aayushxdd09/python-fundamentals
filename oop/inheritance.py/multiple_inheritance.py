class Employee:
    company = "ITC"
    name = "Default"

    def show(self):
        print(f"The name of the employee is {self.name} and the company is {self.company}")

    def role(self):
        print("Developer")

class Coder:
    language = "Python"

    def printlanguage(self):
        print(f"Here is your language: {self.language}")

class Programmer(Employee, Coder):  #Employee will got read first then coder
   
    company = "ITC Infotech"
    def showlanguage(self):
        print(f"The name of Employee is {self.name} and he is good with {self.language} language")
    
a=Employee()
b=Programmer()
print(a.company)
b.role()
print(b.company)   #If the parent and child bith has the same method, the child's one will be preferred
b.showlanguage()
b.printlanguage()
print(b.language)
