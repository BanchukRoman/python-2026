def log_calls(func):
    def wrapper(args):
        file = open("text.txt", "a")
        file.write(f'{func.__name__}\t')
        result = func(args)
        if result.is_integer():
            file.write(f'{result}')
        else:
            file.write(f'{result:.2f}\n')
        file.close()
    return wrapper

@log_calls
def summa(args):
    return sum(args)

@log_calls
def difference(args):
    return args[0] - args[1]

@log_calls
def multiplication(args):
    return args[0] * args[1]

@log_calls
def division(args):
    return args[0] / args[1]

@log_calls
def power(args):
    return args[0] ** args[1]



math_operation = {
    '1': 'Сумма',
    '2': 'Разность',
    '3': 'Произведение',
    '4': 'Деление',
    '5': 'Возведение в степень'
}

for key,value in math_operation.items():
    print(f'{key} -- {value}')

operation_choice_input = input('Введите номер мат операции: ')
nums_input = input('Введите через пробел числа: ').split()
nums = [int(float(num)) if float(num).is_integer() else float(num) for num in nums_input]


match operation_choice_input:
    case '1':
        summa(nums)

    case '2':

        difference(nums)
    case '3':

        multiplication(nums)
    case '4':

        division(nums)
    case '5':
        power(nums)






