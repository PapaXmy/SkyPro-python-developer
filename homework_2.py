user_name = input('Привет!\nПредлогаю проверить свои знания английского!\nРасскажи, как тебя зовут!\n') # ввод имени пользователем
count_question = 0 # счетчик вопросов
count_correct_answer = 0 # счетчик правельных ответов
count_points = 0 # счетчик баллов
points = 0 # быллы

print(f'Привет, {user_name}, начинаем тренировку!')

user_answer_1 = input('My name ___ Vova.\n') # ввод пользователем ответа вопрос
count_question += 1

# проверка ответа пользователя

if user_answer_1 == 'is':
    count_correct_answer += 1
    score = points + 10
    count_points += 10
    print(f'Ответ верный!\nВы получаете {score} балов!')
else:
    print('Неправильно.\nПравильный ответ: is')

user_answer_2 = input('I ___ a coder.\n')
count_question += 1

if user_answer_2 == 'am':
    count_correct_answer += 1
    score = points + 10
    count_points += 10
    print(f'Ответ верный!\nВы получаете {score} балов!')
else:
    print('Неправильно.\nПравильный ответ: am')

user_answer_3 = input('I live ___ Moscow.\n')
count_question += 1

if user_answer_3 == 'in':
    count_correct_answer += 1
    score = points + 10
    count_points += 10
    print(f'Ответ верный!\nВы получаете {score} балов!')
else:
    print('Неправильно.\nПравильный ответ: in')

percent = 100 / count_question * count_correct_answer # сколько процентов по отвеченым правильно вопросов
percent_round = round(percent, 2) # округление до 2го знака
# проверка аписания "вопросов", "вопрос", "вопроса"

if 5 <= count_question <= 20:
    question = 'вопросов'
elif count_question % 10 == 1:
    question = 'вопрос'
elif 2 <= count_question <= 4:
    question = 'вопроса'
else:
    question = 'вопросов'

print(f'Вот и все, {user_name}!\nВы ответили на {count_question} {question} из них {count_correct_answer} верно.\nВы заработали {count_points} баллов.\nЭто {percent_round} процентов.')




