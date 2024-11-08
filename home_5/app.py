from functions import read_file, get_mixing_word, write_history, get_statistic

points = 0

print('Давайте поиграем в игру. Будет загадано слово, вы должны отгадать.')
user_name = input('Введите ваше имя:\n').lower()

for word in read_file():
    user_input = input(f'Угадайте слово: {get_mixing_word(word)}\n')
    if user_input == word:
        points += 10
        print('Верно! Вы получаете 10 очков.')
    else:
        print(f'Неверно! Верный ответ - {word}')

write_history(f'{user_name} {points}')
print(get_statistic())
