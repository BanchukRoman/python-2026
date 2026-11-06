a_input = int(input('Введите число а: '))
b_input = int(input('Введите число b: '))
print(f'сумма a и b = {a_input+b_input}\n'
      f'разность a и b = {a_input-b_input}\n'
      f'произведение a и b = {a_input*b_input}\n'
      f'результат возведения числа a в степень b = {a_input**b_input}')
if b_input != 0:
    print(f'частное от деления a на b = {a_input/b_input:.2f}\n'
          f'остаток от деления a на b = {a_input%b_input}')
else:
    print('При b=0 выполнить деление и деление с остатком невозможно')