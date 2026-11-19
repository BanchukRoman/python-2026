
class Faculty:

    def __init__(self, name):
        self.name = name
        self.departments = set()
        self.students = {}
    def __str__(self):
        return f'На факультете {self.name} есть кафедры {self.departments}'

    def add_student(self, student, specialization_name = None, term = 1):
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
            student.disciplines.clear()
            student.status = 'отчислен'
            student.resits = 0
            student.specialization = None
            student.term = 0

    def add_student_to_discipline(self, student, discipline):
        is_available = any(department.can_teach_discipline(student.specialization, discipline) for department in self.departments)
        if not is_available and student.specialization is not None:
            print(f'\033[31m{discipline.name} не ведется для этой специальности\033[0m')
            return False
        elif student.specialization is None:
            print('\033[31mУ студента нет специальности\033[0m')
            return False
        else:
            print(f'\033[35mСтудент {student.name} записан на дисциплину {discipline.name}\033[0m')
            student.disciplines[discipline] = None
            return True

    @staticmethod
    def remove_student_from_discipline(student, discipline,):
        if discipline in student.disciplines.keys():
            del student.disciplines[discipline]
            print('\033[35mСтудент успешно удален из дисциплины\033[0m')
            return True
        else:
            print('\033[31mСтудента нет на этой дисциплине\033[0m')
            return False

    @staticmethod
    def add_mark_to_discipline(student, discipline, mark,flag):

        if (discipline in student.disciplines.keys()
                and ((student.disciplines[discipline] is None and flag == 'Новая отметка')
                     or (student.disciplines[discipline] is not None and flag == 'Перезапись отметки'))):
            if 0 <= mark <= 10:
                student.disciplines[discipline] = mark
                return True
            else:
                print('\033[31mУ нас 10-ти бальная система\033[0m')
                return False
        elif (discipline in student.disciplines.keys() and (student.disciplines[discipline] is not None and flag == 'Новая отметка')
        or (student.disciplines[discipline] is None and flag == 'Перезапись отметки')):
            print('\033[31mФлаг не соответствует действию\033[0m')
            return False
        else:
            print(f'\033[31mСтудент {student.name} не изучает дисциплину: {discipline.name}\033[0m')
            return False

    def transfer_to_next_term(self, student):
        none_count = 0
        for mark in student.disciplines.values():
            if mark is not None and mark < 4:
                student.resits += 1
            elif mark is None:

                none_count += 1
        if student.resits>=3:
            self.remove_students(student)
            print(f'\033[31mСтудент: {student.name} отчислен\033[0m')
        elif student.resits != 0:
            print(f'\033[31mСтудент: {student.name} получил пересдач: {student.resits}\033[0m ')

            student.term += 1
        elif none_count != 0:
            print(f'\033[31mСтудент: {student.name} не закончил: {none_count} дисциплин\033[0m')
        else:
            print(f'\033[31mСтудент: {student.name} переходит в следующий семестр\033[0m')
            student.term += 1


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
        discipline.depart_name = self.name

    def __repr__(self):
        return self.name

    def __str__(self):
        return f'Кафедра {self.name}'

    def can_teach_discipline(self,specialization_name ,discipline):
        return discipline in self.specializations.get(specialization_name, set())

class Discipline:
    def __init__(self, name):
        self.name = name
        self.depart_name = None
    def __repr__(self):
        return f'{self.depart_name}: Дисциплина: {self.name}'

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.id = student_id
        self.resits = 0
        self.term = 0
        self.status = None
        self.specialization = None
        self.disciplines = {}

    def __repr__(self):
        return f'ID: {self.id} Студент: {self.name} Специальность: {self.specialization} Семестр: {self.term} Пересдач: {self.resits} Статус: {self.status}'

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
bsu_rfict.add_student(banchuk, 'Прикладная информатика')
bsu_rfict.add_student(aksenov, )
bsu_rfict.add_student(petrov, 'Кибербезопасность')

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
    10:'Выход из программы',
    11:'Получение ведомости в файл',
    12:'Получение ведомости по определенной дисциплине в файл',
    13:'Список отчисленных студентов',
    14:'Закрытие пересдач'
}
while True:
    for people in bsu_rfict.students.values():
        if people.status == 'зачислен':
            print(people)
    try:
        student_id_choice_input = int(input('Введите id нужного вам студента: '))
        if bsu_rfict.students[student_id_choice_input].status == 'зачислен':
            while True:
                print('Опции')
                for key, value in options.items():
                    print(f'{key}: {value}')
                try:
                    option_input = int(input('Выберите номер опции: '))
                except ValueError:
                    print('\033[31mНужно ввести число\033[0m')
                    continue
                match option_input:
                    case 1:
                        for key, value in specializations.items():
                            print(f'{key}: {value}')
                        try:
                            specialization_input = int(input('Выберите номер специальности: '))
                        except ValueError:
                            print('\033[31mНужно ввести число\033[0m')
                            continue
                        if specialization_input in specializations.keys():
                            bsu_rfict.add_student(student=bsu_rfict.students[student_id_choice_input], specialization_name=specializations[specialization_input])
                        else:
                            print('\033[31mВы ввели некорректный номер специальности\033[0m')
                    case 2:
                        print(f'\033[31mСтудент {bsu_rfict.students[student_id_choice_input].name} отчислен\033[0m')
                        bsu_rfict.remove_students(bsu_rfict.students[student_id_choice_input])
                        break
                    case 3:
                        print('\033[35mДисциплины\033[0m')
                        for key, value in disciplines_set.items():
                            print(f'{key}: {value}')
                        try:
                            disciplines_choice_input = int(input('Введите номер дисциплины:'))
                            bsu_rfict.add_student_to_discipline(bsu_rfict.students[student_id_choice_input],
                                                                disciplines_set[disciplines_choice_input])
                        except ValueError:
                            print('\033[31mНужно ввести число\033[0m')
                            continue
                        except KeyError:
                            print('\033[31mВы ввели номер несуществующей дисциплины\033[0m')
                            continue

                    case 4:
                        print(f'\033[35mДисциплины студента: {bsu_rfict.students[student_id_choice_input].name}\033[0m')
                        for key, value in disciplines_set.items():
                            if value in bsu_rfict.students[student_id_choice_input].disciplines.keys():
                                print(f'{key}: {value}')
                        try:
                            disciplines_choice_input = int(input('Введите номер дисциплины:'))
                            Faculty.remove_student_from_discipline(bsu_rfict.students[student_id_choice_input],
                                                                   disciplines_set[disciplines_choice_input])
                        except ValueError:
                            print('\033[31mНужно ввести число\033[0m')
                            continue
                        except KeyError:
                            print('\033[31mВы ввели номер несуществующей дисциплины\033[0m')
                            continue



                    case 5:
                        print(f'\033[35mДисциплины студента: {bsu_rfict.students[student_id_choice_input].name}\033[0m')
                        for key, value in disciplines_set.items():
                            if (value in bsu_rfict.students[student_id_choice_input].disciplines.keys()
                                    and bsu_rfict.students[student_id_choice_input].disciplines[value] is None):
                                print(f'{key}: {value}')
                        try:
                            disciplines_choice_input = int(input('Введите номер дисциплины:'))
                            mark_input = int(input('Введите отметку за дисциплину:'))

                            Faculty.add_mark_to_discipline(bsu_rfict.students[student_id_choice_input],
                                                           disciplines_set[disciplines_choice_input], mark_input, 'Новая отметка')
                        except ValueError:
                            print('\033[31mНужно ввести число\033[0m')
                            continue
                        except KeyError:
                            print('\033[31mВы ввели номер несуществующей дисциплины\033[0m')
                            continue


                    case 6:
                        bsu_rfict.transfer_to_next_term(bsu_rfict.students[student_id_choice_input])

                    case 7:
                        print(f'\033[35mУспеваемость студента: {bsu_rfict.students[student_id_choice_input].name}\033[0m')
                        if bsu_rfict.students[student_id_choice_input].disciplines:
                            for key, value in bsu_rfict.students[student_id_choice_input].disciplines.items():
                                print(f'{key.name}: \033[33m{value}\033[0m')
                        else:
                            print('\033[31mСтудент не изучает ни одной дисциплины\033[0m')

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
                    case 11:
                        avg = 0
                        mark_count = 0
                        with open('text.txt', 'w', encoding='utf-8') as f:


                            f.write(f'\tВедомость\n '
                                    f'{bsu_rfict.students[student_id_choice_input]}\n'
                                    f'\tДисциплины\n')
                            for key, value in bsu_rfict.students[student_id_choice_input].disciplines.items():
                                f.write(f'{key}: {value}\n')
                                if value is not None:
                                    mark_count += 1
                                    avg += value
                            try:
                                mark_avg = avg / mark_count
                                f.write(f'Средний балл: {mark_avg:.2f}\n')
                            except ZeroDivisionError:
                                f.write('Нет отметок\n')
                    case 12:
                        print('Дисциплины')

                        for key, value in disciplines_set.items():
                            print(f'{key}: {value.name}')
                        try:
                            disciplines_choice_input = int(input('Введите номер дисциплины:'))
                            avg = 0
                            people_count = 0
                            with open('text.txt', 'w', encoding='utf-8') as f:
                                f.write('Ведомость дисциплины\n')
                                f.write(f'{disciplines_set[disciplines_choice_input]}\n'
                                        f'Студенты изучившие дисциплину:\n')
                                for people in bsu_rfict.students.values():
                                    if disciplines_set[disciplines_choice_input] in people.disciplines.keys() and \
                                            people.disciplines[
                                                disciplines_set[disciplines_choice_input]] is not None:
                                        f.write(f'{people.name}\n')
                                        avg += people.disciplines[disciplines_set[disciplines_choice_input]]
                                        people_count += 1
                                if people_count == 0:
                                    f.write('Нет студентов изучивших дисциплину\n')
                                try:
                                    mark_avg = avg / people_count
                                    f.write(f'Средний балл: {mark_avg:.2f}\n')
                                except ZeroDivisionError:
                                    f.write('Нет отметок\n')
                        except ValueError:
                            print('\033[31mНужно ввести число\033[0m')
                            continue
                        except KeyError:
                            print('\033[31mВы ввели номер несуществующей дисциплины\033[0m')
                            continue

                    case 13:
                        print('\033[35mСписок отчисленных студентов\033[0m')
                        for people in bsu_rfict.students.values():
                            if people.status == 'отчислен':
                                print(f'ID: {people.id} Студент: {people.name}')
                    case 14:
                        print(f'\033[35mПредметы с пересдачей у {bsu_rfict.students[student_id_choice_input].name}\033[0m')
                        for key, value in disciplines_set.items():
                            if (value in bsu_rfict.students[student_id_choice_input].disciplines.keys()
                                    and bsu_rfict.students[student_id_choice_input].disciplines[value] < 4):
                                print(f'{key}: {value}')
                        try:
                            disciplines_choice_input = int(input('Введите номер дисциплины:'))
                            mark_input = int(input('Введите отметку за дисциплину:'))
                            result = Faculty.add_mark_to_discipline(bsu_rfict.students[student_id_choice_input],
                                                           disciplines_set[disciplines_choice_input], mark_input, 'Перезапись отметки')

                            if result and mark_input >= 4:
                                bsu_rfict.students[student_id_choice_input].resits -= 1
                                print(f'Пересдача по {disciplines_set[disciplines_choice_input]} закрыта успешно')

                        except ValueError:
                            print('\033[31mНужно ввести число\033[0m')
                            continue
                        except KeyError:
                            print('\033[31mВы ввели номер несуществующей дисциплины\033[0m')
                            continue
        else:
            print('\033[31mВведите id зачисленного студента\033[0m')
    except ValueError:
        print('\033[31mНужно ввести число\033[0m')
        continue
    except KeyError:
        print('\033[31mВы ввели номер несуществующего студента\033[0m')
        continue


