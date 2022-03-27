class Person:
    def __init__(self, name, family, age, nationality):
        self.name = name
        self.family = family
        self.age = age
        self.nationality = nationality

    def printit(self):
        print(self.name, self.nationality)

class Student(Person):
    def __init__(self, name, family, age, nationality, university, yearofstudy, fac_no):
        super().__init__(name, family, age, nationality)
        self.university = university
        self.yearofstudy = yearofstudy
        self.fac_no = fac_no

    def printit(self):
        print(self.name, self.nationality, self.university, self.yearofstudy)

students = dict()

class Lecturer(Person):
    def __init__(self, name, family, age, nationality, workplace, experience):
        super().__init__(name, family, age, nationality)
        self.workplace = workplace
        self.experience = experience

    def printit(self):
        print(f' {self.name} {self.family} works at {self.workplace} with {self.experience} years experience has students {students}')

    def AddStudent(self,fac_no):
        students[fac_no] = 0

    def SetGrade(self,fac_no,grade):
        students[fac_no] = grade

    def AverageGrade(self):
        average = 0
        sum = 0
        studcount = 0
        for k,v in students.items():
            sum+=v
            studcount+=1
        average = f'{(sum/studcount):.2f}'
        print(average)

Lecture1 = Lecturer('Ivan','Ivanov', 50, 'bulgarian', 'Sofia University', '25')

Lecture1.AddStudent(121)
Lecture1.AddStudent(122)
Lecture1.AddStudent(123)
Lecture1.AddStudent(124)
Lecture1.AddStudent(125)
Lecture1.AddStudent(126)
Lecture1.SetGrade(121,6)
Lecture1.SetGrade(122,4)
Lecture1.SetGrade(123,3)
Lecture1.SetGrade(124,3.5)
Lecture1.SetGrade(125,5.5)
Lecture1.printit()
Lecture1.AverageGrade()