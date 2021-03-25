class Student:

    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.grades = []

    def add_grade(self, grade):
        if type(grade) == Grade:
            self.grades.append(grade)

    def __repr__(self):
        return "I am {name}, year {year}".format(name = self.name, year = self.year)


roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)


class Grade:
    minimum_passing = 65

    def __init__(self, score):
        self.score = score


pieter_grades = Grade(100)
pieter.add_grade(pieter_grades)



print(pieter)
print(sandro)
print(roger)