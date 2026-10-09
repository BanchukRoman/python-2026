a_input = int(input('Введите число а: '))
b_input = int(input('Введите число b: '))
print(f'a+b = {a_input+b_input}\n'
      f'a-b = {a_input-b_input}\n'
      f'a*b = {a_input*b_input}\n'
      f'a^b = {a_input**b_input}')
if b_input != 0:
    print(f'a/b = {a_input/b_input}\n'
          f'a%b = {a_input%b_input}')
else:
    print('При b=0 выполнить деление и деление с остатком невозможно')