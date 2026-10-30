while True:
    hb_day_input = input('Введите дату рождения в формате дд.мм.гггг: ')
    hb_day = int(hb_day_input[:2])
    hb_month = int(hb_day_input[3:5])
    if hb_day <= 0 or hb_month <= 0:
        print('Введите корректную дату')
        continue
    hb_year = int(hb_day_input[6:10])

    if hb_year % 4 == 0:
        leap_year_day = 29
    else:
        leap_year_day = 28
    if (hb_month == 1 and 31 >= hb_day >=20) or (hb_month == 2 and hb_day <=18):
        print('Водолей')
        break
    elif (hb_month == 2 and leap_year_day >= hb_day >=19) or (hb_month == 3 and hb_day <=20):
        print('Рыбы')
        break
    elif (hb_month == 3 and 31 >= hb_day >=21) or (hb_month == 4 and hb_day <=19):
        print('Овен')
        break
    elif (hb_month == 4 and 30 >= hb_day >=20) or (hb_month == 5 and hb_day <=20):
        print('Телец')
        break
    elif (hb_month == 5 and 31 >= hb_day >=19) or (hb_month == 6 and hb_day <=20):
        print('Близнецы')
        break
    elif (hb_month == 6 and 30 >= hb_day >=21) or (hb_month == 7 and hb_day <=22):
        print('Рак')
        break
    elif (hb_month == 7 and 31 >= hb_day >=23) or (hb_month == 8 and hb_day <=22):
        print('Лев')
        break
    elif (hb_month == 8 and 31 >= hb_day >=23) or (hb_month == 9 and hb_day <=22):
        print('Дева')
        break
    elif (hb_month == 9 and 30 >= hb_day >=23) or (hb_month == 10 and hb_day <=22):
        print('Весы')
        break
    elif (hb_month == 10 and 31 >= hb_day >=23) or (hb_month == 11 and hb_day <=21):
        print('Скорпион')
        break
    elif (hb_month == 11 and 30 >= hb_day >=22) or (hb_month == 12 and hb_day <=21):
        print('Стрелец')
        break
    elif (hb_month == 12 and 31 >= hb_day >=22) or (hb_month == 1 and hb_day <=29):
        print('Козерог')
        break
    else:
        print('Дата введена неверно')