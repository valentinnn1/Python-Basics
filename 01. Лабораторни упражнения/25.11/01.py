class Person:
    def __init__(self, name, family, age, nationality):
        self.name = name
        self.family = family
        self.age = age
        self.nationality = nationality

    def printit(self):
        print(self.name, self.nationality)


Person1 = Person("Valentin", "Popov", 18, "bulgarian")
Person2 = Person("Ivan", "Ivanov", 32, "bulgarian")
Person3 = Person("Olivia", "Black", 22, "english")

Person1.printit()
Person2.printit()
Person3.printit()