from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/add', methods=["POST"])
def add():
    print(request.form['title'])
    print(request.form['desc'])

    return render_template('index.html', add = 1)
