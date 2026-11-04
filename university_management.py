
class University:
    pass

class Department:
    def __init__(self, name):
        self.name = name
        self.disciplines = []




# class Specialization:
#     pass

class Discipline:
    def __init__(self, name):
        self.name = name

class Student:
    def __init__(self, name, admission_score ):
        self.name = name
        self.admission_score = admission_score
        self.specialization = None

    def __str__(self):
        return f'Студент: {self.name} специальность: {self.specialization}'

    def go_to_specialization(self, specialization):
        self.specialization = specialization


student1 = Student("Банчук Р.В.", 365)
student2 = Student("Аксенов Р.В.", 320)
student3 = Student("Петров Р.В.", 390)
students = [
    student1,
    student2,
    student3
]
specializations = [
    'Прикладная информатика',
    'Кибербезопасность',
    'Интеллектуальная электроника',
    'Радиофизика'
]
for student in students:
    if student.admission_score < 300:
        print(f'{student.name} не зачислен')
    elif 300 <= student.admission_score < 325:
        student.go_to_specialization(specializations[3])
        print(student)
    elif 325 <= student.admission_score < 350:
        student.go_to_specialization(specializations[2])
        print(student)
    elif 350 <= student.admission_score < 375:
        student.go_to_specialization(specializations[1])
        print(student)
    elif 375 <= student.admission_score < 400:
        student.go_to_specialization(specializations[0])
        print(student)

