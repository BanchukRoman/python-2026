money_input = int(input('Введите вашу сумму денег: '))
count_100 = money_input // 100
count_50 = money_input % 100 // 50
count_10 = money_input % 100 % 50 // 10
count_5 = money_input % 100 % 50 % 10 // 5
count_2 = money_input % 100 % 50 % 10 % 5 // 2
count_1 = money_input % 100 % 50 % 10 % 5 % 2 // 1
print(f"кол-во каждого номинала: 100-{count_100} 50-{count_50} 10-{count_10} 5-{count_5} 2-{count_2} 1-{count_1}")


money = [100 , 50 , 10 , 5 , 2 , 1 ]
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

for key, value in dict(zip(money,result)).items():
    print(f"Номинал {key} встречается - {value} раз(а)")