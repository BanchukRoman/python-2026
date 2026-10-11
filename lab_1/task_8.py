import random

secret_num = random.randint(1, 100)

while True:
    answer_input = int(input('Введите ваше число от 1 до 100: '))
    if answer_input < secret_num:
        print('Ваше число меньше')
        continue
    elif answer_input > secret_num:
        print('Ваше число больше')
        continue

    if answer_input == secret_num:
        print('Вы угадали')
        again = input('Не хотите сыграть сыграть еще раз? да\нет')
        if again == 'да':
            secret_num = random.randint(1, 100)
            print('Число загадано')
            continue
        else:
            break
