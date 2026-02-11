class Employee:
    
    language = "python"
    salary = 120000

    def __init__(self, name, salary, language):    #Its called dunder method and gets called automatically
        
        self.name = name
        self.salary = salary
        self.language = language
        
        print("I am creating an object")

    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")


harry = Employee("Harry", 130000, "Javascript")

harry.getinfo()
print(harry.name, harry.language)



