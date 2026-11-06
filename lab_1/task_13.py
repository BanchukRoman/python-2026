numbers_input = input('Введите числа через пробел: ').split(' ')
numbers = [int(float(num)) if float(num).is_integer() else float(num) for num in numbers_input]


# numbers = []
# for number in numbers_input:
#     if number.isdigit():
#         numbers.append(int(number))
#     else:
#         numbers.append(float(number))

numbers_dict = dict()
for num in set(numbers):
    numbers_dict[num] = numbers.count(num)

unique_numbers = [num for num in numbers_dict if numbers_dict[num] == 1]
repeat_numbers = [num for num in numbers_dict if numbers_dict[num] > 1]

even_numbers = [num for num in numbers_dict if num % 2 == 0]
uneven_numbers = [num for num in numbers_dict if num % 2 == 1]
negative_numbers = [num for num in numbers_dict if num < 0]
float_numbers = [num for num in numbers_dict if not num.is_integer()]

multiple_of_five = [num for num in numbers_dict if num % 5 == 0]
print(f'Уникальные числа: \033[31m {unique_numbers} \033[0m')
print(f'Повторяющиеся числа: \033[31m{repeat_numbers} \033[0m')
print(f'Четные числа: \033[31m {even_numbers} \033[0m')
print(f'Нечетные числа: \033[31m{uneven_numbers} \033[0m')
print(f'Отрицательные числа: \033[31m{negative_numbers} \033[0m')
print(f'Числа с точкой: \033[31m{float_numbers} \033[0m')
print(f'Сумма кратных пяти: \033[31m{sum(multiple_of_five)} \033[0m')
print(f'Самое большое число: \033[31m{max(numbers)} \033[0m')
print(f'Самое маленькое число: \033[31m{min(numbers)} \033[0m')