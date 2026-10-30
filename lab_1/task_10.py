
input_age = int(input("Возраст клиента: "))
input_amount = float(input("Сумма в чеке: "))
input_is_hb = input("У клиента день рождения да/нет: ")
input_is_vip = input("Клиент VIP ? да/нет: ")
is_hb = True if input_is_hb == "да" else False
is_vip = True if input_is_vip == "да" else False
vip_discount = 15
discount = 0
if input_amount > 1000:
    discount += 10
if input_age >= 63:
    discount += 5
if is_hb:
    discount += 5
if is_vip:
    if vip_discount >= discount:
        discount = vip_discount
else:
    if discount >= 10:
        discount = 10
finish_amount = input_amount - input_amount * discount / 100
print(f"Вы получаете скидку {discount} %, к оплате {finish_amount} руб")