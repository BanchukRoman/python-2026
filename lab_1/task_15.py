products = [
    {'name': 'Клюшка Bauer', 'price': 800, 'sales': 1},
    {'name': 'Клюшка CCM', 'price': 600, 'sales': 2},
    {'name': 'Клюшка Bauer', 'price': 800, 'sales': 1},
    {'name': 'Клюшка Zaryad', 'price': 250, 'sales': 1},
    {'name': 'Клюшка Bauer', 'price': 800, 'sales': 1},
    {'name': 'Клюшка CCM', 'price': 600, 'sales': 2},
    {'name': 'Клюшка CCM', 'price': 600, 'sales': 1},
]
total_gain = 0
for product in products:
    total_gain += product['price'] * product['sales']
unique_names = set([product['name'] for product in products])
print(f'Общая выручка: \033[31m{total_gain}\033[0m BYN')
unique_products = dict()
for name in unique_names:
    unique_products[name] = sum([product['sales'] * product['price'] for product in products if product['name'] == name])

max_gain_value = max(unique_products[name] for name in unique_names)
max_gain_name = [name for name in unique_names if unique_products[name] == max_gain_value]
print(f'Самый большой доход получен с товара(ов): \033[35m{', '.join(max_gain_name)}\033[0m')

print(f'Всего уникальных наименований \033[36m{len(unique_names)}\033[0m')