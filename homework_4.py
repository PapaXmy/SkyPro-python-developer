'''домашняя работа по спискам'''

# объявление списков со словами по уровню сложности
words_easy = {
    "family":"семья",
    "hand": "рука",
    "people":"люди",
    "evening": "вечер",
    "minute":"минута",
}

words_medium = {
    "believe":"верить",
    "feel": "чувствовать",
    "make":"делать",
    "open": "открывать",
    "think":"думать",
}

words_hard   = {
    "rural":"деревенский",
    "fortune": "удача",
    "exercise":"упражнение",
    "suggest": "предлагать",
    "except":"кроме",
}

# список уровней сложности для подсчета ранга
levels = {
   0: "Нулевой",
   1: "Так себе",
   2: "Можно лучше",
   3: "Норм",
   4: "Хорошо",
   5: "Отлично",
}

# список уровней сложности, в значении ключа лежит список с соответствующим списком по сложности
difficulty_level = {
    'Легкий': words_easy,
    'Средний': words_medium,
    'Сложный': words_hard
}
answers = {} # пустой список для формирования вывода правильных и неправильных ответов
choice_user = {} # список выбора пользователем уровня сложности
rank = 0 # переменная для подсчета правильных ответов для формирования ранга пользователя
properly_distracted = [] # список для формирования списка парвильных ответов
not_properly_distracted = [] # список для формирования списка не парвильных ответов

# выбор пользователем уровня сложности
user_choice = input('Выберите уровень сложности.\n'
                    'Легкий, средний, сложный.\n').capitalize()
while True:
    if user_choice.capitalize() == 'Легкий':
        break
    elif user_choice.capitalize() == 'Средний':
        break
    elif user_choice.capitalize() == 'Сложный':
        break
    else:
        user_choice = input('Уровень сложности выбран не верно.'
                            'Попробуйте еще раз.\n').capitalize()

for k, v in difficulty_level.items():
    if user_choice == k:
        choice_user = v
        user_answer = input('Выбран уровень сложности, мы предложим 5 слов, подберите перевод.\n'
                            'Нажмите Enter ')

# итерация по вопросам согласно выбранного уровня сложности пользователем
for k, v in choice_user.items():
    user_answer = input(f'{k}, {len(v)} букв, начинается на {v[0]}...\n').lower()

    # проверка слова пользователя, если в ответе ничего нет вопрос задается заново
    while True:
        if user_answer == '':
            user_answer = input('Тут ничего нет. Попробуйте еще раз!\n')
        else:

            if user_answer == v:
                print(f'Верно, {k} - это {v}.')
                answers[k] = True
                rank += 1
                break

            print(f'Неверно. {k} - это {v}.')
            answers[k] = False
            break

# формирование отчета об отвеченых словах пользователя
for key, value in answers.items():
    if value == True:
        properly_distracted.append(key)
    else:
        not_properly_distracted.append(key)

if properly_distracted == []:
    print('')
else:
    print('Правильно отвечены слова:')
    [print(word) for word in properly_distracted]
if not_properly_distracted == []:
    print('')
else:
    print('Неправильно отвеченые слова:')
    [print(word) for word in not_properly_distracted]

for key, value in levels.items():
    if rank == key:
        print(f'Ваш ранг:\n{value} ')
