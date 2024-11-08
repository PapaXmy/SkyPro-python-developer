from player import Player
from utils import load_random_word

def main():
    # ввод игроком имени
    name_player = input('Давайте поиграем в слова. Введите ваше имя:\n')
    # создание нового игрока
    player = Player(name_player)

    print(f'Привет, {player.name_player}!')

    # загрузка слов через requests
    words = load_random_word()

    # задаем игроку слово из которого нужно составить слова
    print(f'Составьте {words.count_subwords()} слов из слова "{words.word}"\n'
          f'Слова должны быть не короче 3х букв\n'
          f'Чтобы закончить игру, угадайте все слова или напишите "стоп"')

    print('Поехали, ваше первое слово:')

    while True:
        player_word = input()
        # прверки вводимого слова игроком
        if player_word.lower() == 'стоп':
            break
        # проверка длины слова
        if len(player_word) < 3:
            print('Слишком короткое слово')
        # проверка использовалось ли слово ранее
        elif player.check_used_word(player_word):
            print('Слово уже использовано')
        # проверка слова есть ли оно в списке подслов
        elif words.check_subwords(player_word) is not True:
            print('Неверно')
        # проверка все ли слова составлены
        elif len(player.used_words) == len(words.subwords):
            break
        else:
            # добавление слова в список составленных слов игроком
            if words.check_subwords(player_word) is True:
                player.used_words_player(player_word)
                print('Верно')

    print(f'Игра завершена, вы угадали {player.count_used_words()} слов!')

if __name__ == '__main__':
    main()
