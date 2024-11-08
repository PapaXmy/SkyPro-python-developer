from functions import load_question, statistic
import random

def main():

    print('Игра начинается!')

    questions = load_question()

    for question in questions:
        print(f'{question.build_question()}')
        user_input = input('Ваш ответ: ').lower()

        question.user_answer = user_input
        question.question_asked = True

        print(question.feedback())

    print('Вот и все!')
    print(statistic(questions))

if __name__ == '__main__':
    main()
