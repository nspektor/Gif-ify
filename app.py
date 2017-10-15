from flask import Flask
from flask import render_template
from nytimesarticle import articleAPI
import json
import os

app = Flask(__name__)

subject = ""
api = articleAPI('28bba9543b494e2f9d15976a0fa44f5c')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/category/')
def category():
    return render_template('category.html')

@app.route('/category/<name>')
def hello_name(name):
    subject = name
    return 'link: %s!' % getUrls()


def getUrls():
    result = []
    articles = api.search( fq='The New York Times', begin_date='20171010', fl='web_url', sort='newest', facet_field=subject, facet_filter='true')
    data = json.dumps(articles)
    parsed_json = json.loads(data)
    for i in range(0,6):
        result.append(parsed_json["response"]["docs"][i]["web_url"])
    return result

if __name__ == '__main__':
    app.debug = True
    app.run()
