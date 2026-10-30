money_input = int(input('Введите вашу сумму денег: '))
count_100 = money_input // 100
count_50 = money_input % 100 // 50
count_20 = money_input % 100 % 50 // 20
count_10 = money_input % 100 % 50 % 20 // 10
count_5 = money_input % 100 % 50 % 20 % 10 // 5
count_2 = money_input % 100 % 50 % 20 % 10 % 5 // 2
count_1 = money_input % 100 % 50 % 20 % 10 % 5 % 2 // 1
print(f"кол-во купюр каждого номинала для {money_input}р\n"
      f"по 100р - {count_100} \n"
      f"по 50р - {count_50} \n"
      f"по 20р - {count_20} \n"
      f"по 10р - {count_10} \n"
      f"по 5р - {count_5} \n"
      f"по 2р - {count_2} \n"
      f"по 1р - {count_1} \n")


money = [100 , 50 , 20, 10 , 5 , 2 , 1 ]
result = []
new_money = 0
for i in range(len(money)):
    if i == 0:
        new_money = money_input // 100
        result.append(new_money)
    else:
        new_money = money_input % money[i-1] // money[i]
        money_input = money_input % money[i-1]
        result.append(new_money)
print(f"кол-во купюр каждого номинала для {money_input}р")
for key, value in dict(zip(money,result)).items():
    print(f"Номинал {key} встречается - {value} раз(а)")