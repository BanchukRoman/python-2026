salary_input = float(input('Введите вашу зп: '))
apartment_rental_input = float(input('Введите стоимость аренды жилья: '))
food_expenses_input = float(input('Введите траты на питание: '))
transportation_costs_input = float(input('Введите траты на транспорт: '))
fun_costs_input = float(input('Введите траты на развлечения: '))
sport_costs = float(input('Введите траты на спорт: '))

ideal_coefficients = {
    'apartment_rental': .3,
    'food_expenses': .2,
    'transportation_costs': .1,
    'fun_costs': .1,
    'sport_costs': .05,
    'savings': .25
}
list_of_costs = [
    apartment_rental_input,
    food_expenses_input,
    transportation_costs_input,
    fun_costs_input,
    sport_costs
]
savings = salary_input
for cost in list_of_costs:
    savings -= cost

if apartment_rental_input / salary_input > ideal_coefficients['apartment_rental']:
    print(f'Вы переплачиваете за жилья, желательно тратить не более {ideal_coefficients["apartment_rental"] * salary_input} BYN' )

if food_expenses_input / salary_input > ideal_coefficients['food_expenses']:
    print(f'Вы переплачиваете за питание, желательно тратить не более {ideal_coefficients["food_expenses"] * salary_input} BYN')

if transportation_costs_input / salary_input > ideal_coefficients['transportation_costs']:
    print(f'Вы переплачиваете за транспорт, желательно тратить не более {ideal_coefficients["transportation_costs"] * salary_input} BYN')

if fun_costs_input / salary_input > ideal_coefficients['fun_costs']:
    print(f'Вы переплачиваете за развлечения, желательно тратить не более {ideal_coefficients["fun_costs"] * salary_input} BYN')

if sport_costs / salary_input > ideal_coefficients['sport_costs']:
    print(f'Вы переплачиваете за спорт, желательно тратить не более {ideal_coefficients["sport_costs"] * salary_input} BYN')

if savings / salary_input <= 0:
    print('Вы вообще не откладываете деньги, а возможно уходите в долг, это очень плохо и в будущем может доставить кучу проблем')
elif savings / salary_input < ideal_coefficients['savings']:
    print('Вы откладываете меньше 25%, желательно учесть советы выше и обеспечить себя надежной подушкой безопасности')
else:
    print(f'Вы откладываете 25% и более,что составляет {savings}BYN это прекрасный показатель')






