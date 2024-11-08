import requests, json
from utils import Question



def load_question():
    '''Загрузка вопросов с интернета при помощи requests
    '''
    questions = []
    response = requests.get('https://api.npoint.io/04a50342a7b4b7e4d74c')
    data = json.loads(response.text)

    for text in data:
        question = Question(text['q'],int(text['d']), text['a'])
        questions.append(question)

    return questions

def statistic(questions):
    '''Статистика на основе списка объектов класса Question
    '''
    correct, total, score = 0, 0, 0

    for question in questions:
        total += 1 # сколько всего вопросов задано
        if question.is_correct():
            correct += 1 # на сколько вопросов правильно отвечено
            score += question.point # сколько баллов за вопросы начислено

    return f'Отвечено {correct} вопроса из {total}\nНабрано баллов: {score}'
