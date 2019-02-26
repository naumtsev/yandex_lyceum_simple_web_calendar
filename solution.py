from flask import Flask, render_template, request, redirect
import json
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField
from wtforms.validators import DataRequired


class RadioCalendar(FlaskForm):
    certification = RadioField('certification', choices=[(1, 'Прогноз на завтра'), (2, 'Прогноз на 3 дня'), (3, 'Прогноз на месяц')])
    submit = SubmitField('Получить прогноз')

info = json.loads(open('static/days.json', 'r', encoding='utf-8').read())

print(info)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e70lIUUoXRKlXc5VUBmiJ9Hdi'


@app.route('/day1', methods=['GET', 'POST'])
def day1():
    cnt = 0
    p1 = {}
    for p in info:
        cnt += 1
        p1[p] = info[p]
        if cnt == 1:
            break
    return render_template('day1.html', days=p1, text='Прогноз погоды на завтра')


@app.route('/day3', methods=['GET', 'POST'])
def day3():
    cnt = 0
    p1 = {}
    for p in info:
        cnt += 1
        p1[p] = info[p]
        if cnt == 3:
            break
    return render_template('day1.html', days=p1, text='Прогноз погоды на три дня')


@app.route('/day30', methods=['GET', 'POST'])
def day30():
    cnt = 0
    p1 = [[]]
    buff = 0
    for p in info:
        cnt += 1
        buff += 1
        p1[-1].append((p, info[p]['average_temperature']))

        if(buff == 7):
            buff = 0
            p1.append([])



        if(cnt == 30):
            break
    return render_template('day30.html', days=p1)

@app.route('/', methods=['GET', 'POST'])
def index():
    my_form = RadioCalendar()
    data = my_form.certification.data
    if data == '1':
        return redirect('/day1')

    elif data == '2':
        return redirect('/day3')
    elif data == '3':
        return redirect('/day30')

    #if my_form.validate_on_submit():

    return render_template('index.html', form=my_form)






if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')