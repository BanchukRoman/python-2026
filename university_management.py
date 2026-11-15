from itertools import count


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
            student.status = 'зачислен'
            student.term = term
        elif student.specialization is None:
            student.specialization = specialization_name
            student.status = 'зачислен'
            student.term = term

    def remove_students(self,student):
        if student.id in self.students.keys():
            del self.students[student.id]
            student.specialization = None
            student.term = None
            student.status = 'отчислен'

    def add_student_to_discipline(self, student, discipline):
        is_available = any(department.can_teach_discipline(student.specialization, discipline) for department in self.departments)
        if not is_available:
            print(f'{discipline.name} не ведется для этой специальности')
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

    def transfer_to_next_term(self, student):
        attestation = True
        resit_count = 0
        for mark in student.disciplines.values():
            if mark is not None and mark < 4:
                resit_count += 1
            elif mark is None:
                attestation = False
        if resit_count>=3:
            self.remove_students(student)
            print(f'Студент: {student.name} отчислен')
            attestation = False
        elif resit_count != 0:
            print(f'Студент: {student.name} получил пересдач: {resit_count} ')
        if attestation:
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
        return f'Кафедра {self.name}'

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
    3:'Радиофизика'
}
bsu_rfict = Faculty('РФиКТ')
bsu_rfict.add_students(banchuk, 'Прикладная информатика')
bsu_rfict.add_students(aksenov, )
bsu_rfict.add_students(petrov, 'Кибербезопасность')

math = Discipline('Матанализ')
diskretka = Discipline('Дискретная математика')
vibecoding = Discipline('Вайбкодинг')
agila = Discipline('АГиЛА')
ml = Discipline('Машинное обучение')
data_base = Discipline('Базы данных')

disciplines_set = {
    1:math,
    2:diskretka,
    3:vibecoding,
    4:agila,
    5:ml,
    6:data_base}

department1 = Department('Интеллектуальные системы')
department2 = Department('Анализ больших данных')
department3 = Department('Кафедра высшей математики')

bsu_rfict.add_department(department1)
bsu_rfict.add_department(department2)
bsu_rfict.add_department(department3)


department1.add_discipline_to_specialization(specialization_name='Кибербезопасность',discipline=vibecoding)
department1.add_discipline_to_specialization(specialization_name='Радиофизика',discipline=vibecoding)
department1.add_discipline_to_specialization(specialization_name='Прикладная информатика',discipline=vibecoding)
department1.add_discipline_to_specialization(specialization_name='Прикладная информатика',discipline=ml)

department2.add_discipline_to_specialization(specialization_name='Прикладная информатика',discipline=data_base)
department2.add_discipline_to_specialization(specialization_name='Кибербезопасность',discipline=data_base)

department3.add_discipline_to_specialization(specialization_name='Кибербезопасность',discipline= math)
department3.add_discipline_to_specialization(specialization_name='Кибербезопасность',discipline=agila)
department3.add_discipline_to_specialization(specialization_name='Кибербезопасность',discipline=diskretka)

department3.add_discipline_to_specialization(specialization_name='Прикладная информатика',discipline= math)
department3.add_discipline_to_specialization(specialization_name='Прикладная информатика',discipline=agila)
department3.add_discipline_to_specialization(specialization_name='Прикладная информатика',discipline=diskretka)

department3.add_discipline_to_specialization(specialization_name='Радиофизика',discipline= math)
department3.add_discipline_to_specialization(specialization_name='Радиофизика',discipline=agila)


options = {
    1:'Зачисление студента на специальность',
    2:'Отчисление студента',
    3:'Добавление студента для изучения дисциплины',
    4:'Удаление студента из списка изучающих дисциплину',
    5:'Выставление отметки студенту за изученную дисциплину',
    6:'Перевод студента в следующий семестр',
    7:'Успеваемость студента',
    8:'Просмотр дисциплин по кафедрам',
    9:'Выбор другого студента',
    10:'Выход из программы'
}
while True:
    for people in bsu_rfict.students.values():
        print(people)
    student_id_choice_input = int(input('Введите id нужного вам студента: '))
    while True:
        print('Опции')
        for key, value in options.items():
            print(f'{key}: {value}')
        option_input = int(input('Выберите номер опции: '))
        match option_input:
            case 1:
                for key, value in specializations.items():
                    print(f'{key}: {value}')
                specialization_input = int(input('Выберите номер специальности: '))
                bsu_rfict.add_students(student=bsu_rfict.students[student_id_choice_input], specialization_name=specializations[specialization_input])
            case 2:
                bsu_rfict.remove_students(bsu_rfict.students[student_id_choice_input])
                print(f'{bsu_rfict.students[student_id_choice_input]} отчислен')
            case 3:
                print('\033[31mДисциплины\033[0m')
                for key, value in disciplines_set.items():
                    print(f'{key}: {value}')
                disciplines_choice_input = int(input('Введите номер дисциплины:'))
                bsu_rfict.add_student_to_discipline(bsu_rfict.students[student_id_choice_input], disciplines_set[disciplines_choice_input])
            case 4:
                print(f'\033[31mДисциплины студента: {bsu_rfict.students[student_id_choice_input].name}\033[0m')
                for key, value in disciplines_set.items():
                    if value in bsu_rfict.students[student_id_choice_input].disciplines.keys():
                        print(f'{key}: {value}')

                disciplines_choice_input = int(input('Введите номер дисциплины:'))
                Faculty.remove_student_from_discipline(bsu_rfict.students[student_id_choice_input],disciplines_set[disciplines_choice_input])
            case 5:
                print(f'\033[31mДисциплины студента: {bsu_rfict.students[student_id_choice_input].name}\033[0m')
                for key, value in disciplines_set.items():
                    if value in bsu_rfict.students[student_id_choice_input].disciplines.keys():
                        print(f'{key}: {value}')
                disciplines_choice_input = int(input('Введите номер дисциплины:'))
                mark_input = int(input('Введите отметку за дисциплину:'))
                Faculty.add_mark_to_discipline(bsu_rfict.students[student_id_choice_input],disciplines_set[disciplines_choice_input], mark_input)
            case 6:
                bsu_rfict.transfer_to_next_term(bsu_rfict.students[student_id_choice_input])

            case 7:
                print(f'\033[31mУспеваемость студента: {bsu_rfict.students[student_id_choice_input].name}\033[0m')
                for key, value in bsu_rfict.students[student_id_choice_input].disciplines.items():
                    print(f'{key}: \033[33m{value}\033[0m')

            case 8:
                for  depart in bsu_rfict.departments:
                    print(f'{depart}:')
                    list_disciplines = []
                    for value in depart.specializations.values():
                        for element in value:
                            list_disciplines.append(element)

                    print(f'Дисциплины: {set(list_disciplines)}')

            case 9:
                break
            case 10:
                exit()










