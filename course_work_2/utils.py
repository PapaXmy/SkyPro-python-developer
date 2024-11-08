import requests, random, json
from basic_word import BasicWord

def load_random_word():
    '''
    Функция загрузки слов через requests возвращает экземпляр класса WordBasic
    '''
    # загрузка слов с внешнего источника
    response = requests.get('https://api.npoint.io/8b15361a3518bded0f0a')
    # получение слов в виде json
    list_words = response.json()
    # получение одного случайного слова и json
    random_word = random.choice(list_words)
    # создание экземпляра класса WordBasic
    basic_word = BasicWord(random_word['word'], random_word['subwords'])

    return basic_word
