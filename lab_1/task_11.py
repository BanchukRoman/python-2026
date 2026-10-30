SUBSISTENCE_MINIMUM = 868
age_input = int(input('Введите возраст клиента: '))
salary_input = float(input('Введите вашу зп: '))
loan_amount_input = float(input('Введите сумму кредита: '))
loan_term_input = int(input('Введите срок кредита в месяцах: '))
credit_history_input = input('Кредитная история отличная/хорошая/удовлетворительная/плохая: ')
is_guarantors_input = input('Есть ли поручители да/нет: ').lower()
is_deposit_input = input('Есть ли залог да/нет: ').lower()

is_guarantors = True if is_guarantors_input == 'да' else False
is_deposit = True if is_deposit_input == 'да' else False
if age_input <= 21 or age_input > 58 or salary_input <= SUBSISTENCE_MINIMUM:
    print('Отказ в кредите')
    exit()

dti = (loan_amount_input / loan_term_input) / salary_input * 100
print(f'\nСоотношение кредита к доходу: {dti:.2f}% ')
risk_coefficient = 0
if not is_guarantors:
    risk_coefficient += 1
if not is_deposit:
    risk_coefficient += 1
if dti >= 90:
    risk_coefficient += 6
elif dti >= 60:
    risk_coefficient += 5
elif dti >= 40:
    risk_coefficient += 4
elif dti >= 30:
    risk_coefficient += 2
elif dti >= 20:
    risk_coefficient += 1
match credit_history_input:
    case 'отличная':
        risk_coefficient -= 2
    case 'хорошая':
        risk_coefficient -= 1
    case 'удовлетворительная':
        risk_coefficient += 1
    case 'плохая':
        risk_coefficient += 2
if age_input + loan_term_input / 12 > 63:
    risk_coefficient += 3
elif age_input + loan_term_input / 12 > 50:
    risk_coefficient += 2
elif age_input + loan_term_input / 12 > 40:
    risk_coefficient += 1

risk_category = ''
if 1 > risk_coefficient >= -2:
    risk_category = 'низкий'
elif 4 > risk_coefficient >= 1:
    risk_category = 'средний'
elif 7 > risk_coefficient >= 4:
    risk_category = 'высокий'
elif risk_coefficient >= 7:
    risk_category = 'критический'
print(f'Риск: {risk_category}')
print(f'Процентная ставка {12 + risk_coefficient * .5:.2f}%')
if 6 > risk_coefficient >= -2:
    print('\033[32mМожно одобрить\033[0m')
elif risk_coefficient >= 6:
    print('\033[31mОдобрение под сомнением\033[0m')