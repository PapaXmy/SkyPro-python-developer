class Player:
    '''Класс игрока при инициализации задается имя и пустой список используемых слов'''

    def __init__(self, name_player):
        self.name_player = name_player
        self.used_words = []


    def used_words_player(self, word):
        '''
        Добавление слова игрока в список используемых слов
        '''
        self.used_words.append(word)


    def count_used_words(self):
        '''
        Метод возвращает длину списка угаданных слов
        '''
        return len(self.used_words)


    def check_used_word(self, check_word):
        '''
        Проверка есть ли вводимое слово в с списке отгаданых слов
        '''
        for word in self.used_words:
            if check_word == word:
                return True
        return False


    def __repr__(self):
        return self.name_player
