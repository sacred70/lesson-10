# coding: utf8
from functions import load_candidates
from functions import get_by_pk
from functions import get_by_skill_2
from functions import get_all_2
from flask import Flask


app = Flask(__name__)


@app.route("/")
def page_index():
    return get_all_2()


@app.route("/candidates/<x>")
def candidates(x):
    return get_by_pk(text=load_candidates(), pk=int(x))


@app.route("/skills/<x>")
def skills(x):
    return get_by_skill_2(text=load_candidates(), skill_name=x)


app.run()

