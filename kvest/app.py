from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def page_index():
    user_data = [
        {
        'name': 'Egor',
        'age': 10,
        'number': 123456
    },
        {'name': 'maksim',
         'age': 38,
         'number': 12342121

         },
        {
            'name': 'dania',
            'age': 40,
            'number': 12321216
        }
    ]
    return render_template('index.html',
                           users=user_data)


@app.route('/p1')
def page_p1():
    return render_template('p1.html')


app.run(debug=True)
