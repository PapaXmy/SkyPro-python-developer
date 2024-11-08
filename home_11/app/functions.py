import json

def load_candidates():
    '''
    Загружает всех кандидатов из json
    '''
    with open('app/candidates.json', 'r') as file:
        json_candidates = file.read()
        candidates = json.loads(json_candidates)

        return candidates


def get_by_id(id):
    '''
    Возвращает кандидата по порядковому номеру
    '''
    for candidates in load_candidates():
        if candidates['id'] == id:
            return candidates

def get_by_name(name):
    '''
    Возвращает кандидатов по имени
    '''
    name_list = []
    for candidates in load_candidates():
        if name.lower() in candidates['name'].lower().split(' '):
            name_list.append(candidates)

    return name_list

def get_by_skills(skills):
    '''
    Возвращает кандидатов по его скилам
    '''
    candidates_skills_list = []
    for candidates in load_candidates():
        if skills.lower() in candidates['skills'].lower().split(', '):
            candidates_skills_list.append(candidates)

    return candidates_skills_list