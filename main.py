from flask import Flask, render_template

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


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')

