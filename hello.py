from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Ghun2 Hello, World! you must go to sleep !'