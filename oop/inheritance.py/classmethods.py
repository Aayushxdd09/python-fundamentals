class Employee:
    a = 1

    @classmethod   #Allows to take class attribute instead of instance or object
    def show(cls):
        print(f"Class attribute is {cls.a}")

e = Employee()
e.a = 45
#It will not show instance attribut as we have given classmethod decorator
e.show()


class Parent:
    name = "Parent"

    @classmethod
    def show(cls):
        print(cls.name)

class Child(Parent):
    name = "Child"

Child.show() 
#It works on class rather than object
