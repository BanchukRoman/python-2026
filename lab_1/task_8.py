import random

secret_num = random.randint(1, 100)
red = "\033[31m"
green = "\033[32m"
purple = "\033[35m"
cyan = "\033[36m"
reset = "\033[0m"

while True:
    answer_input = int(input(f'{purple}Введите ваше число от 1 до 100: {reset}'))
    if answer_input < secret_num:
        print(f'{red}Ваше число меньше{reset}')
        continue
    elif answer_input > secret_num:
        print(f'{red}Ваше число больше{reset}')
        continue

    if answer_input == secret_num:
        print(f'{green}Вы угадали{reset}')
        again = input(f'{cyan}Не хотите сыграть сыграть еще раз? да\нет: {reset}')
        if again == 'да':
            secret_num = random.randint(1, 100)
            print(f'{cyan}Число загадано{reset}')
            continue
        else:
            print(f'{red}Будем ждать вас снова{reset}')
            break
