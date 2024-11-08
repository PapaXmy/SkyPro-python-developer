import requests, json

class Question:
    '''Класс вопросов
    '''
    def __init__(self, text_question, complexity, correct_answer):
        self.text_question = text_question
        self.complexity = complexity
        self.correct_answer = correct_answer
        self.question_asked = False
        self.user_answer = None
        self.point = complexity * 10

    def get_points(self):
        '''Возвращает колличество баллов в зависимости от сложности вопроса
        '''
        return self.point

    def is_correct(self):
        '''
        Возвращает True если ответ пользователя правильный
        '''
        return self.correct_answer == self.user_answer


    def build_question(self):
        '''
        Возвращае вопрос в нужном виде
        '''
        return f'Вопрос: {self.text_question}\nСложность {self.complexity}/5'

    def feedback(self):
        '''Возвращает верный или нет ответ пользователя
        '''
        if self.is_correct():
            return f'Ответ верный, получено {self.get_points()} баллов'
        return f'Ответ неверный, верный ответ {self.correct_answer}'
