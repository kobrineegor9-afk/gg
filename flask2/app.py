from flask import Flask, render_template

app  = Flask(__name__)
@app.route('/')
def pageindex():

    return render_template('index.html' ,name='7777')


@app.route('/p1')
def page_p1():
    return render_template('p1.html')

app.run(debug = True)