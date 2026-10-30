user_input = input('Введите слово(строку): ')
user_input_r = user_input[::-1]
if user_input_r == user_input:
    print('Это полиндром')
else:
    print('Это не полиндром')