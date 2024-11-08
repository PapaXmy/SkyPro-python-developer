import json

def load_candidates():
    '''
    Загружает всех кандидатов из json
    '''
    with open('app/candidates.json', 'r') as file:
        json_candidates = file.read()
        candidates = json.loads(json_candidates)

        return candidates


def get_by_pk(pk):
    '''
    Возвращает кандидата по порядковому номеру
    '''
    for candidates in load_candidates():
        if candidates['pk'] == pk:

            return candidates


def get_by_skills(skills):
    '''
    Возвращает кандидатов по его скилам
    '''
    candidates_skills_list = []
    for candidates in load_candidates():
        if skills.lower() in candidates['skills'].lower().split(', '):
            candidates_skills_list.append(candidates)

    return candidates_skills_list


def content(candidates):
    '''
    Возвращает спиок кандидато в нужном нам виде
    '''
    page = ''
    for candidate in candidates:
        page += candidate['name'] + '\n'
        page += candidate['position'] + '\n'
        page += candidate['skills'] + '\n'
    return '<pre>' + page + '</pre>'
