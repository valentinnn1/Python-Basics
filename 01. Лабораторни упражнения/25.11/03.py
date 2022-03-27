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


class Student(Person):
    def __init__(self, name, family, age, nationality, university, yearofstudy):
        super().__init__(name, family, age, nationality)
        self.university = university
        self.yearofstudy = yearofstudy

    def printit(self):
        print(self.name, self.nationality, self.university, self.yearofstudy)


Person4 = Student("Valentin", "Popov", 19, "bulgarian",
                  "Technical University", 1)
Person5 = Student("Ivan", "Ivanov", 22, "bulgarian", "UNWE", 4)
Person6 = Student("Olivia", "Black", 20, "american", "Harvard University", 2)

Person4.printit()
Person5.printit()
Person6.printit()

class Lecturer(Person):
    def __init__(self, name, family, age, nationality, workplace, experience):
        super().__init__(name, family, age, nationality)
        self.workplace = workplace
        self.experience = experience

    def printit(self):
        print(f'{self.name} {self.family} works at {self.workplace} with {self.experience} years experience!')


Lecture1 = Lecturer("Ivan", "Ivanov", 50, "bulgarian", "Technical University", 25)
Lecture2 = Lecturer("Maria", "Petrova", 35, "bulgarian", "Sofia University", 8)
Lecture3 = Lecturer("Petar", "Iliev", 45, "bulgarian", "Sofia University", 18)
Lecture1.printit()
Lecture2.printit()
Lecture3.printit()