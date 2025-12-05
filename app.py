
from flask import Flask, render_template
import json

app = Flask(__name__)


# Загружаем данные из JSON файла
def load_candidates():
    with open('candidates.json', 'r', encoding='utf-8') as file:
        return json.load(file)


# Главная страница
@app.route('/')
def index():
    candidates = load_candidates()

    # Формируем текст для отображения в теге <pre>
    candidates_text = ""
    for candidate in candidates:
        candidates_text += f"Имя кандидата - {candidate['name']}\n"
        candidates_text += f"Позиция кандидата - {candidate['position']}\n"
        candidates_text += f"Навыки через запятую - {candidate['skills']}\n\n"

    return f"<pre>{candidates_text}</pre>"


# Страница кандидата
@app.route('/candidate/<int:candidate_id>')
def candidate_profile(candidate_id):
    candidates = load_candidates()

    # Ищем кандидата по ID
    candidate = None
    for cand in candidates:
        if cand['id'] == candidate_id:
            candidate = cand
            break

    if candidate is None:
        return "Кандидат не найден"

    # Формируем HTML для отображения кандидата
    return f"""
    <img src="{candidate['picture']}" width=200>
    <pre>
    Имя кандидата - {candidate['name']}
    Позиция кандидата - {candidate['position']}
    Навыки через запятую - {candidate['skills']}
    </pre>
    """


# Поиск по навыкам
@app.route('/skill/<skill_name>')
def search_by_skill(skill_name):
    candidates = load_candidates()

    # Ищем кандидатов с указанным навыком (регистронезависимо)
    matching_candidates = []
    for candidate in candidates:
        # Приводим навыки к нижнему регистру для регистронезависимого поиска
        skills = candidate['skills'].lower().split(', ')
        if skill_name.lower() in skills:
            matching_candidates.append(candidate)

    if not matching_candidates_age:
        return "Кандидаты с таким навыком не найдены"

    # Формируем список найденных кандидатов
    result_text = f"<h2>Кандидаты с навыком '{skill_name}':</h2>"
    for candidate in matching_candidates:
        result_text += f"<pre>"
        result_text += f"Имя кандидата - {candidate['name']}\n"
        result_text += f"Позиция кандидата - {candidate['position']}\n"
        result_text += f"Навыки через запятую - {candidate['skills']}\n"
        result_text += f"</pre><br>"

    return result_text
@app.route('/age/<int:age>')
def search_by_age(age):
    candidates = load_candidates()
    matching_candidates_age = []
    for candidate in candidates:
        ages = candidate['age']
        if age == ages:
            matching_candidates_age.append(candidate)




if __name__ == '__main__':
    app.run(debug=True)
