products = [
    {'name': 'Клюшка Bauer', 'price': 800, 'sales': 32},
    {'name': 'Клюшка CCM', 'price': 600, 'sales': 45},
    {'name': 'Клюшка Soyuz', 'price': 400, 'sales': 135},
    {'name': 'Клюшка Zaryad', 'price': 250, 'sales': 21},
]
total_gain = 0
for product in products:
    total_gain += product['price'] * product['sales']

print(f'Общая выручка: \033[31m{total_gain}\033[0m BYN')
max_gain_value = max(product['sales'] * product['price'] for product in products)
max_gain_list = [product['name'] for product in products if product['sales'] * product['price'] == max_gain_value]
print(f'Самый большой доход получен с товара(ов): \033[35m{', '.join(max_gain_list)}\033[0m')
unique_names = set([product['name'] for product in products])
print(f'Всего уникальных наименований \033[36m{len(unique_names)}\033[0m')