class Employee:
    
    language = "python"
    salary = 120000

    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning!")

harry = Employee()
harry.language= "JavaScript"

harry.getinfo() 
#harry.getinfo will convert into employee.getinfo(harry) but we have not given any argument in line 6 "getinfo()" so we put it as self, else it would give an error.

harry.greet()
#We have marked it as static method so it won't take argument

