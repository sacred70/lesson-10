# coding: utf8
import json


def load_candidates(file="candidates.json"):
    # загрузит данные из файла
    with open(file, "r", encoding='utf-8') as f:
        text_ = json.load(f)
        return text_


def get_by_pk(text=load_candidates(), pk=int):
    # вернет кандидата по pk
    for i in text:
        if i['pk'] == pk:
            return f"<img src='{i['picture']}'\n> " \
                   f"<pre>\n" \
                   f"Имя кандидата - {i['name']}\n" \
                   f"{i['position']}\n" \
                   f"{i['skills']}\n" \
                   f"</pre>"

    return "Такого кандидата нет в списке"


def get_all_2(text=load_candidates()):
    # покажет всех кандидатов
    count = 0
    return_candidates = ''
    while count <= len(text):
        for i in text:
            count += 1
            return_candidat = f"Имя кандидата - {i['name']}\n" \
                    f"{i['position']}\n" \
                    f"{i['skills']}\n"\

            return_candidates = return_candidates+f'\n{return_candidat}'

        return f'<pre>\n{return_candidates}\n</pre>'


def get_by_skill_2(text=load_candidates(), skill_name=''):
    # вернет кандидатов по навыку
    count = 0
    return_candidates = ''
    s = skill_name.lower()
    while count <= len(text):
        for i in text:
            count += 1
            skill = i['skills']
            t = skill.lower()
            if s in t:
                return_candidat = f"Имя кандидата - {i['name']}\n" \
                       f"{i['position']}\n" \
                       f"{i['skills']}\n"
                return_candidates = return_candidates+f'\n{return_candidat}'

        return f'<pre>\n{return_candidates}\n</pre>'




