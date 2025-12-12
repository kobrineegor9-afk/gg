from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)
history = {}


@app.route('/')
def index():
    global history
    history = {}
    return render_template('index.html')


@app.route('/<int:step>:<int:choice>')
def quest(step, choice):
    global history
    message = ''
    if step == 0:
        message = ('перед тобой 2 дороги. налево пойдешь - золото найдешь, '
                   'направо пойдешь - коня потеряешь. идем налвео?')
    elif step == 1:

        if choice == 1:
            message = ('ты нашел золотую монету.'
                       'видимо остальное кто то уже успел утащить.'
                       'идем в погоню?')
        elif choice == 0:
            message = ('хорошо что ты без коня'
                       'зато здесь один пасется, теперь ты на коне'
                       'начинаем занаво?')
        history['1'] = choice
    elif step == 2:
        if history['1'] == 0:
            if choice == 1:
                return redirect(url_for('index'))
            elif choice == 0:
                return redirect(url_for('quest', step=1, choice=0))
        message = ('уходя за горизонт ты наткнулся на деревню гномов'
                   'глядя на монетку которую ты подидывал они решили что '
                   'теперь тебя ждет каторга на золотых рудниках зато буду'
                   'в золоте в буквальном смысле. начинаем заново?')
        history['2'] = choice
    elif step == 3:
        if choice == 0 and history['2'] == 0:
            return redirect(url_for('quest', step = 2, choice = 0))
        elif choice ==0 and history['2'] == 1:
            return redirect(url_for ('quest', step = 2, choise = 1))
        else:
            return redirect(url_for('index'))

    step += 1
    return render_template('quest.html',
                           message=message,
                           step=step)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=500, debug=True)
