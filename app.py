from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Gifify the News!'


if __name__ == '__main__':
    app.run()
