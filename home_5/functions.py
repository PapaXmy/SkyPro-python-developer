import random

def read_file():
    '''
    Чтение слов из файла
    '''
    with open('words.txt', 'r') as file:
        words_list =[]
        for word in file:
            s = word.rstrip('\n')
            words_list.append(s)

        return words_list


def get_mixing_word(word):
    '''
    Перемешивание букв в слове
    '''
    list_letters = []
    for i in word:
        list_letters.append(i)

    mixing_list = random.shuffle(list_letters)

    return ''.join(list_letters)


def write_history(string):
    '''
    Запись истории игры для вывода статистики
    '''
    with open('history.txt', 'a') as file:

            history_game = file.write(string + '\n')


def get_statistic():
    '''
    Статистика игры на основе истории
    '''
    with open('history.txt', 'r') as file:
        max_points = []

        for value in file:
            name, points = value.rstrip('\n').split(' ')
            max_points.append(points)

        statistics_output = f'Всего игр сыграно: {len(max_points)}\nМаксимальный рекорд: {max(max_points)}'

        return statistics_output
