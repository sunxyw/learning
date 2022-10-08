class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print('Hello, my name is ' + self.name)


class TenYearOldPerson(Person):
    def __init__(self, name):
        super().__init__(name, 10)

    def greet(self):
        print("I don't know how to greet")


tyo = TenYearOldPerson('John')
tyo.greet()
