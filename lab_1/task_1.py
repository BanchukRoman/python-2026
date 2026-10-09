surname_input = input("Введите вашу фамилию: ")
name_input = input("Введите ваше имя: ")
middle_name_input = input("Введите ваше отчество: ")
ready_surname = surname_input[0].upper() + surname_input[1:]
# ready_surname = surname_input.capitalize()
ready_name = name_input[0].upper()
ready_middle_name = middle_name_input[0].upper()
print(f"Ваше Ф.И.О. {ready_surname} {ready_name}.{ready_middle_name}.")