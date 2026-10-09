password = input("Введите пароль: ").replace(" ", "")
if len(password) < 16:
    print('пароль слишком короткий')
elif password.isalpha() or password.isdigit():
    print('очень слабый пароль')
else:
    print('надежный пароль')

# альтернатива
# if len(password) < 16:
#     print('пароль слишком короткий')
# elif password.isalpha():
#     print('очень слабый пароль, тебе стоит добавить чисел')
# elif password.isdigit():
#     print('очень слабый пароль, тебе стоит добавить букв')
# else:
#     print('надежный пароль')