
hb_day_input = input('Введите дату рождения в формате дд.мм.гггг: ')
hb_day = abs(int(hb_day_input[:2]))
hb_month = abs(int(hb_day_input[3:5]))
hb_year = int(hb_day_input[6:10])
if hb_year % 4 == 0:
    leap_year_day = 29
else:
    leap_year_day = 28
if (hb_month == 1 and 31 >= hb_day >=20) or (hb_month == 2 and hb_day <=18):
    print('Водолей')
elif (hb_month == 2 and leap_year_day >= hb_day >=19) or (hb_month == 3 and hb_day <=20):
    print('Рыбы')
elif (hb_month == 3 and 31 >= hb_day >=21) or (hb_month == 4 and hb_day <=19):
    print('Овен')
elif (hb_month == 4 and 30 >= hb_day >=20) or (hb_month == 5 and hb_day <=20):
    print('Телец')
elif (hb_month == 5 and 31 >= hb_day >=19) or (hb_month == 6 and hb_day <=20):
    print('Близнецы')
elif (hb_month == 6 and 30 >= hb_day >=21) or (hb_month == 7 and hb_day <=22):
    print('Рак')
elif (hb_month == 7 and 31 >= hb_day >=23) or (hb_month == 8 and hb_day <=22):
    print('Лев')
elif (hb_month == 8 and 31 >= hb_day >=23) or (hb_month == 9 and hb_day <=22):
    print('Дева')
elif (hb_month == 9 and 30 >= hb_day >=23) or (hb_month == 10 and hb_day <=22):
    print('Весы')
elif (hb_month == 10 and 31 >= hb_day >=23) or (hb_month == 11 and hb_day <=21):
    print('Скорпион')
elif (hb_month == 11 and 30 >= hb_day >=22) or (hb_month == 12 and hb_day <=21):
    print('Стрелец')
elif (hb_month == 12 and 31 >= hb_day >=22) or (hb_month == 1 and hb_day <=29):
    print('Козерог')
else:
    print('Дата введена неверно')