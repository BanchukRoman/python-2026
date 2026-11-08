
class Faculty:

    def __init__(self, name):
        self.name = name
        self.departments = set()
        self.students = {}
    def __str__(self):
        return f'На факультете {self.name} есть кафедры {self.departments}'

    def add_students(self,student, specialization_name):
        if student.id not in self.students.keys():
            self.students[student.id] = student
            student.specialization = specialization_name
            student.status = 'enrolled'



    def remove_students(self,student):
        if student.id in self.students.keys():
            del self.students[student.id]
            student.status = 'expelled'


    def add_student_to_discipline(self, student, discipline):
        is_available = any(department.can_teach_discipline(student.specialization, discipline) for department in self.departments)
        if not is_available:
            print(f'{discipline.name} не ведется ни  на одной кафедре')
            return False
        else:
            print(f'Студент {student.name} записан на дисциплину {discipline.name}')
            student.disciplines[discipline] = None
            return True

    def remove_student_from_discipline(self, student, discipline,):
        if discipline in student.disciplines.keys():
            del student.disciplines[discipline]
            print('Студент успешно удален из дисциплины')
            return True
        else:
            print('Студент а нет на этой дисциплине')
            return False


    def add_department(self, department):
        self.departments.add(department)


class Department:

    def __init__(self, name):
        self.name = name
        self.specializations = {}


    def add_discipline_to_specialization(self,specialization_name ,discipline):
        if specialization_name not in self.specializations:
            self.specializations[specialization_name] = set()
        self.specializations[specialization_name].add(discipline)

    def __repr__(self):
        return self.name

    def __str__(self):
        return f'Кафедра {self.name} -- {self.specializations}'

    def can_teach_discipline(self,specialization_name ,discipline):
        return discipline in self.specializations.get(specialization_name, set())

    # def add_specialization(self, specialization_name):
    #     set_disciplines = set()
    #     self.specializations[specialization_name] = set_disciplines

    # def add_student_to_learn(self, student):
    #     if student.specialization in self.specializations:
    #         student.disciplines[0] = self.disciplines[0]


# class Specialization:
#     pass

class Discipline:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f'{self.name}'


class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.id = student_id
        self.status = None
        self.specialization = None
        self.disciplines = {}

    def __str__(self):
        return f'ID: {self.id} Студент: {self.name} Специальность: {self.specialization} Статус: {self.status}'




student1 = Student("Банчук Р.В.", 365)
student2 = Student("Аксенов Р.В.", 320)
student3 = Student("Петров Р.В.", 390)
students = [
    student1,
    student2,
    student3
]
# specializations = [
#     'Прикладная информатика',
#     'Кибербезопасность',
#     'Интеллектуальная электроника',
#     'Радиофизика'
# ]
bsu_rfict = Faculty('РФиКТ')


math = Discipline('Матанализ')
vibecoding = Discipline('Вайбкодинг')
agila = Discipline('АГиЛА')

department1 = Department('Интеллектуальные системы')
department2 = Department('Анализ больших данных')
department3 = Department('Кафедра высшей математики')
bsu_rfict.add_department(department1)
bsu_rfict.add_department(department2)
bsu_rfict.add_department(department3)

department1.add_discipline_to_specialization(specialization_name='Прикладная информатика',discipline=vibecoding )
department1.add_discipline_to_specialization(specialization_name='Кибербезопасность',discipline= math )
department1.add_discipline_to_specialization(specialization_name='Кибербезопасность',discipline=agila )

# department3.add_discipline_to_specialization(specialization_name='Прикладная информатика',discipline_name='Матанализ')
# department3.add_discipline_to_specialization(specialization_name='Прикладная информатика',discipline_name='АГиЛА')
# department3.add_discipline_to_specialization(specialization_name='Прикладная информатика',discipline_name='Дискретная математика')
# department3.add_discipline_to_specialization(specialization_name='Кибербезопасность',discipline_name='Матанализ')
# department3.add_discipline_to_specialization(specialization_name='Кибербезопасность',discipline_name='АГиЛА')

print(department1)
print(department2)
print(department3)
print(department1.can_teach_discipline('Кибербезопасность',math))# bsu_rfict.add_department(department1)
print(bsu_rfict)

# for student in students:
#     if student.admission_score < 300:
#         print(f'{student.name} не зачислен')
#     elif 300 <= student.admission_score < 325:
#         student.go_to_specialization(specializations[3])
#         print(student)
#     elif 325 <= student.admission_score < 350:
#         student.go_to_specialization(specializations[2])
#         print(student)
#     elif 350 <= student.admission_score < 375:
#         student.go_to_specialization(specializations[1])
#         print(student)
#     elif 375 <= student.admission_score < 400:
#         student.go_to_specialization(specializations[0])
#         print(student)

