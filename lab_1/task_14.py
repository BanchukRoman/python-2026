numbers_input1 = input('Введите числа через пробел: ').split(' ')
numbers1 = set(int(float(num)) if float(num).is_integer() else float(num) for num in numbers_input1)

numbers_input2 = input('Введите числа через пробел: ').split(' ')
numbers2 = set(int(float(num)) if float(num).is_integer() else float(num) for num in numbers_input2)

print(f'Числа в 2 наборах одновременно \033[31m{numbers1 & numbers2}\033[0m')
print(f'Числа из первого набора, которые отсутствуют во втором, и наоборот \033[31m{numbers1 - numbers2} и {numbers2 - numbers1}\033[0m')
print(f'Числа из обоих наборов, за исключением чисел, найденных в пункте 1 \033[31m{numbers1 ^ numbers2}\033[0m')