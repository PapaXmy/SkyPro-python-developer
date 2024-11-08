from app import app
from flask import render_template
from app.functions import *


@app.route("/")
def index():
    """
    Главная страница
    """
    candidates = load_candidates()
    return render_template("index.html", candidates=candidates)


@app.route("/candidate/<int:uid>/")
def candidate_id(uid):
    """
    Страница кандидатов по id
    """
    candidate_id = get_by_id(uid)
    return render_template("card.html", candidate_id=candidate_id)


@app.route("/search/<candidate_name>/")
def search(candidate_name):
    """
    Страница поиска кандидатов
    """
    search_candidate = get_by_name(candidate_name)
    return render_template(
        "search.html", search_candidate=search_candidate, candidate_name=candidate_name
    )


@app.route("/candidate/<skill>/")
def skills_candidate(skill):
    """
    Страница кандидатов по скилам
    """
    skills = get_by_skills(skill)
    return render_template("skills.html", skills=skills, skill=skill)
