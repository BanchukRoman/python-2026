
class Faculty:

    def __init__(self, name):
        self.name = name
        self.departments = set()
        self.students = {}
    def __str__(self):
        return f'На факультете {self.name} есть кафедры {self.departments}'

    def add_students(self,student, specialization_name = None,term = 1):
        if student.id not in self.students.keys():
            self.students[student.id] = student
            student.specialization = specialization_name
            student.status = 'enrolled'
            student.term = term
        elif student.specialization is None:
            student.specialization = specialization_name
            student.status = 'enrolled'
            student.term = term

    def remove_students(self,student):
        if student.id in self.students.keys():
            del self.students[student.id]
            student.specialization = None
            student.term = None
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

    @staticmethod
    def remove_student_from_discipline(student, discipline,):
        if discipline in student.disciplines.keys():
            del student.disciplines[discipline]
            print('Студент успешно удален из дисциплины')
            return True
        else:
            print('Студент а нет на этой дисциплине')
            return False

    @staticmethod
    def add_mark_to_discipline(student, discipline, mark):
        if discipline in student.disciplines.keys():
            student.disciplines[discipline] = mark
            return True
        else:
            print(f'Студент {student.name} не изучает дисциплину: {discipline.name}')
            return False

    def transfer_to_next_term(self,faculty):
        for student in self.students.values():
            for mark in student.disciplines.values():
                if mark < 4:
                    faculty.remove_students(student)
                continue
            student.term +=1

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

class Discipline:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f'{self.name}'

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.id = student_id
        self.term = None
        self.status = None
        self.specialization = None
        self.disciplines = {}

    def __repr__(self):
        return f'ID: {self.id} Студент: {self.name} Специальность: {self.specialization} Семестр: {self.term} Статус: {self.status}'

banchuk = Student("Банчук Р.В.", 365)
aksenov = Student("Аксенов Р.В.", 320)
petrov = Student("Петров Р.В.", 390)
# students = [
#     student1,
#     student2,
#     student3
# ]
specializations = {
    1:'Прикладная информатика',
    2:'Кибербезопасность',
    3:'Интеллектуальная электроника',
    4:'Радиофизика'
}
bsu_rfict = Faculty('РФиКТ')
bsu_rfict.add_students(banchuk, 'Прикладная информатика')
bsu_rfict.add_students(aksenov, )
bsu_rfict.add_students(petrov, 'Кибербезопасность')

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

# print(department1)
# print(department2)
# print(department3)
# print(department1.can_teach_discipline('Кибербезопасность',math))# bsu_rfict.add_department(department1)
# print(bsu_rfict)
options = {
    1: 'Зачисление студента на специальность',
    2:'Отчисление студента',
    3:'Добавление студента для изучения дисциплины',
    4:'Удаление студента из списка изучающих дисциплину',
    5:'Выставление отметки студенту за изученную дисциплину',
    6:'Перевод студента в следующий семестр',
    7:'Выбор другого студента',
    8:'Выход из программы'
}
while True:
    for people in bsu_rfict.students.values():
        print(people)
    student_choice_input = int(input('Введите id нужного вам студента: '))
    print('Опции')
    for key, value in options.items():
        print(f'{key}: {value}')
    option_input = int(input('Выберите номер опции: '))
    match option_input:
        case 1:
            for key, value in specializations.items():
                print(f'{key}: {value}')
            specialization_input = int(input('Выберите номер специальности: '))
            bsu_rfict.add_students(student=bsu_rfict.students[student_choice_input], specialization_name=specializations[specialization_input])
        case 2:
            bsu_rfict.remove_students(bsu_rfict.students[student_choice_input])
            print(f'{bsu_rfict.students[student_choice_input]} отчислен')
        case 3:
            # bsu_rfict.add_student_to_discipline()
            pass

