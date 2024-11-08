import json

def load_students():
    '''
    Загрузка студентов из файла
    '''
    with open('students.json', 'r') as file:
        json_file = file.read()
        json_read = json.loads(json_file)
        return json_read


def load_professions():
    '''
    Загрузка профессий из файла
    '''
    with open('professions.json', 'r') as file:
        json_file = file.read()
        json_read = json.loads(json_file)
        return json_read


def get_students_by_pk(usr_pk):
        '''
        Возвращает студента по порядковому номеру
        '''
        student_list = []

        for students in load_students():

            if usr_pk == students['pk']:
                dict_students = dict(
                    pk=students['pk'],
                    full_name=students['full_name'],
                    skills=students['skills'])
                student_list.append(dict_students)

        return student_list


def get_profession_bay_title(usr_title):
    '''
    Возвращает скилы выбранной профессии
    '''
    profession_list = []

    for title in load_professions():
        if title['title'] == usr_title:
            dict_professions = dict(skills=title['skills'])
            profession_list.append(dict_professions)

    return profession_list


def check_fitness(student, profession):
    '''
    Возвращает словарь с проверкой
    '''
    student = get_students_by_pk(student)
    profession = get_profession_bay_title(profession)
    set_student = set()
    set_profession = set()

    for value in student:

        for skill in value['skills']:
            set_student.add(skill)

    for value in profession:

        for skill in value['skills']:
            set_profession.add(skill)

    skills_intersection = set_student.intersection(set_profession)
    skills_difference = set_profession.difference(set_student)

    if skills_intersection == set():
        fit_percent = 0
    else:
        fit_percent = round(len(skills_intersection) / len(set_profession) * 100)

    check_fitness_dict = {
        'has': list(set_student),
        'lacks': list(skills_difference),
        'fit_percent': int(fit_percent)
    }

    return check_fitness_dict
