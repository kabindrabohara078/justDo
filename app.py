from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['post'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    print(username, password)

    return 'Done fuckoff'

@app.route('/register')
def register(data):
    print(data)

app.run()