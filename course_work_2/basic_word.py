class BasicWord:
    '''Класс загадываемого слова, аргументы само слово и список подслов
    составленных из загадываемого слова'''
    def __init__(self, original_word, subwords):
        self.word = original_word
        self.subwords = subwords


    def check_subwords(self, subword):
        '''
        Метод проверяет есть ли вводимое слово в списке подстрок загадываемого
        слова, возвращает bool
        '''
        for word in self.subwords:
            if word == subword:
                return True
        return False


    def count_subwords(self):
        '''
        Длина списка подстрок
        '''
        return len(self.subwords)


    def __repr__(self):
        return self.word
