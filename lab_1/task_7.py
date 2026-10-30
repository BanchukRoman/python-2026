MINUTES = 60
MEGABYTES = 1000
SMS = 30
TARIFF = 24.99
minutes_input = int(input("Введите сколько минут вы потратили за месяц: "))
megabytes_input = int(input("Введите сколько Mb вы потратили за месяц: "))
sms_input = int(input("Введите сколько sms вы потратили за месяц: "))

if minutes_input <= MINUTES:
    paid_mins = 0
else:
    paid_mins = (minutes_input - MINUTES) * 0.89

# Нужно ли коэффиценты записывать константой?

if megabytes_input <= MEGABYTES:
    paid_megabytes = 0
else:
    paid_megabytes = (megabytes_input-MEGABYTES) * 0.79

paid_sms = 0 if sms_input <= SMS else (sms_input-SMS) * 0.59

total_tariff = TARIFF + paid_mins + paid_megabytes + paid_sms
tax = total_tariff * 0.02
print(f'Базовый тариф {TARIFF} руб')
if paid_mins != 0:
    print(f'Плата за доп минуты: {paid_mins:.2f} руб')
if paid_megabytes != 0:
    print(f'Плата за доп мегабайты: {paid_megabytes:.2f} руб')
if paid_sms != 0:
    print(f'Плата за доп sms: {paid_sms:.2f} руб')
print(f'Налог: {tax:.2f} руб')
print(f'Общая стоимость: {total_tariff + tax:.2f} руб')
# лучше использовать round или в ф строках можно и :.2f?