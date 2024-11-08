from app import app
from app.functions import*

@app.route('/')
def index():
    '''
    Главная страница
    '''
    page = content(load_candidates())
    return page

@app.route('/candidate/<int:uid>')
def candidate_id(uid):
    '''
    Страница кандидатов по id
    '''
    candidate = get_by_pk(uid)
    list_candidate = [candidate]
    page = content(list_candidate)
    return page


@app.route('/candidate/<skills>')
def skills_candidate(skills):
    '''
    Страница кандидатов по скилам
    '''
    candidates = get_by_skills(skills)
    page = content(candidates)
    return page
