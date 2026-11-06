type_input = input("Выберите тип измерения время/расстояние/скорость: ")
units = {
    'время':'с/мин/ч/сут',
    'расстояние': 'см/дм/м/км/миля',
    'скорость': 'м/с / км/ч / миль/ч'
}
start_unit_choice = input(f"Введите исходную единицу {units[type_input]}: ")
final_unit_choice = input(f"Введите конечную единицу {units[type_input]}: ")
value_input = float(input('Введите значению для перевода: '))


unit_convert = {
    'с': 1,
    'мин' : 60,
    'ч' : 3600 ,
    'сут': 86400,
    'см': 0.01,
    'дм': 0.1,
    'м': 1,
    'км': 1000,
    'м/с': 1 ,
    'км/ч': 0.278,
    'миль/ч': 0.447
}

# if final_unit_choice == 'с' and (start_unit_choice == 'мин' or start_unit_choice == 'ч' or start_unit_choice == 'сутки'):
#     print(f'перевод из {value_input} {start_unit_choice} в {final_unit_choice}: {value_input * unit_convert[start_unit_choice]}')

convert_result = value_input * unit_convert[start_unit_choice] / unit_convert[final_unit_choice]
print(f'перевод: {value_input} {start_unit_choice} = {convert_result:.2f} {final_unit_choice}')