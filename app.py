from flask import Flask
from flask import render_template
import urllib,json

import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return 'Hello, World'


data = json.loads(urllib.urlopen("http://api.giphy.com/v1/gifs/search?q=ryan+gosling&api_key=TN5SAJ5tC9a68o8fm1jdqG0hXO2rMNct&limit=5").read())
print json.dumps(data, sort_keys=True, indent=4)


if __name__ == '__main__':
    app.debug = True
    app.run()
