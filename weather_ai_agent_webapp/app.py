from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Weather AI Agent Web App!"

@app.route('/login')
def login():
    return "Login Page"
app.run(debug=True)

