text_input = input("Введите ваш текст: ").lower()
symbols = ['.',',', '!', '?', ',' , '*', '+', '*', '/', '%', '#', '&', ';', ':']

text_for_copy = ('Этот текст удобно скопировать для проверки задания и в целом сразу будет видно как работает этот код')

for symbol in symbols:
    text_input = str(text_input.replace(symbol, ''))
all_words = text_input.split(' ')
for i in range(2):
    total_words = len(all_words)
    print(f'\033[31mВсего слов: {total_words} \033[0m')
    common_words = dict()

    for word in set(all_words):
        print(f'Слово \033[35m{word}\033[0m встречается {all_words.count(word)} раз')
        common_words[word] = all_words.count(word)

    max_value = max(common_words.values())
    most_common_word = [key for key, value in common_words.items() if value == max_value]
    print(f'Больше всего встретилось: \033[35m{', '.join(most_common_word)}\033[0m')
    len_of_words = dict()


    max_len = len(max(common_words.keys(), key = len))
    biggest_word = [word for word in common_words.keys() if len(word) == max_len]
    min_len = len(min(common_words.keys(), key = len))
    smallest_word = [word for word in common_words.keys() if len(word) == min_len]

    print(f'Больше всех по длине: \033[35m{', '.join(biggest_word)}\033[0m\n'
          f'Меньше всех по длине: \033[35m{', '.join(smallest_word)}\033[0m\n')

    filtered_words = [word for word in all_words if len(word) >= 3 ]
    all_words = filtered_words


