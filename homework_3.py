questions = ["My name ___  Vova\n", "I ___ a coder\n", "I live ___ Moscow\n"]
answers = ["is", "am", "in"]
count_questions = 0
count_correct_answers = 0
number_attempt = 2
persent  = 0
points = 0


user_input = input('Привет!\n'
                   'Прелогаю проверить свои знания английского!\n'
                   'Наберите "ready", чтобы начать!\n')

if user_input.lower() == 'ready':
    for question in range(len(questions)):
        user_answer = input(questions[question])

        if user_answer == answers[question]:

            count_questions += 1
            count_correct_answers += 1
            points += 3
            print('Ответ верный!')
        else:

            attempt = number_attempt
            while attempt != 0:
                print(f'Осталось попыток: {attempt}, попробуйте еще раз!')
                attempt -= 1
                user_answer = input(questions[question])

                if user_answer == answers[question]:
                    print('Ответ верный!')
                    points += 2
                    break
                else:
                    while attempt != 0:
                        print(f'Осталось попыток: {attempt}, попробуйте еще раз!')
                        attempt -= 1
                        user_answer = input(questions[question])

                        if user_answer == answers[question]:
                            print('Ответ верный!')
                            points += 1
                        else:
                            print(f'Увы, но нет. Правильный ответ: {answers[question]}')

            count_questions +=1

    if 5 <= count_questions <= 20:
        word_end = 'вопросов'
    elif count_questions % 10 == 1:
        word_end = 'вопрос'
    elif 2 <= count_questions <= 4:
        word_end = 'вопроса'
    else:
        word_end = 'вопросов'

    if 5 <= points <= 20:
        point = 'баллов'
    elif points % 10 == 1:
        point = 'балл'
    elif 2 <= points <= 4:
        point = 'балла'
    else:
        point = 'баллов'

    print(f'Вот и все! Вы ответили на {count_questions} {word_end} из них {count_correct_answers} верно, это {points} {point}.')

else:
    print('Кажется вы не хотите играть. Очень жаль.')




