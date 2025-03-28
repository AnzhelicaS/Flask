from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route('/<string:title>')
@app.route('/index<string:title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/list_prof/<list>')
def list_function(list):
    list_prof = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач',
                 'инженер по терраформированию', 'климатолог', 'специалист по радиационной защите',
                 'астрогеолог', 'гляциолог', 'пилот дронов', 'штурман', 'метеоролог']
    return render_template('index.html', index=list, list=list_prof)


@app.route('/auto_answer')
@app.route('/answer')
def answer():
    dict_info = {'Фамилия': 'Watny', 'Имя': 'Mark', 'Образование': 'выше среднего', 'Профессия': 'штурман марсохода',
                 'Пол': 'male', 'Мотивация': 'Всегда мечтал застрять на Марсе!', 'Готовы остаться на Марсе?': 'True'}
    title = 'Анкета'
    return render_template('auto_answer.html', title=title, dict=dict_info)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/distribution')
def distribution():
    people_list = ['Редли Скотт', 'Энди Уир', 'Тони Старк', 'Наташа Романов', 'Стив Роджерс', 'Ник Фьюри']
    return render_template('distribution.html', people_list=people_list)


@app.route('/table/<gender>/<age>')
def table(gender, age):
    return render_template('table.html', gender=gender, age=int(age))


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')
