from flask import Flask
from flask import render_template
from nytimesarticle import articleAPI
import json
import urllib,json
import os
import requests

app = Flask(__name__)


api = articleAPI('7adeb932f30043dea8bd262313d00d3c')
urls = []
keywords = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/category/')
def category():
    return render_template('category.html')

@app.route('/category/<name>')
def hello_name(name):
    subject = name.capitalize()
    print(subject)
    getUrls(subject)
    words = []
    for i in range(len(urls)):
        print(urls[i] + " " + keywords[i])
        splitHead = keywords[0].split(' ')
        word = splitHead[0]
        words.append(word)

    url = "https://api.giphy.com/v1/gifs/translate"

    s=word[0]

    querystring = {"api_key":"TN5SAJ5tC9a68o8fm1jdqG0hXO2rMNct","s":s}

    response = requests.request("GET", url, params=querystring)
    jsonR = response.json()
    data = json.dumps(jsonR)
    parsed_json = json.loads(data)
    theURL = parsed_json["data"]["embed_url"]
    return render_template('category.html', url=theURL)


def getUrls(subject):
    articles = api.search( fq='The New York Times', begin_date='20171010', fl='web_url, section_name, headline', facet_field='section_name')
    data = json.dumps(articles)
    parsed_json = json.loads(data)
    i = 0
    while i < 10:
        result = parsed_json["response"]["docs"][i]
        #print(result)
        print(result["section_name"])
        if(result["section_name"] == subject):
            urls.append(result['web_url'])

            keywords.append(result['headline']['main'])
            print("ADDED")
        i += 1
    print(urls[0])



data = json.loads(urllib.urlopen("http://api.giphy.com/v1/gifs/search?q=ryan+gosling&api_key=TN5SAJ5tC9a68o8fm1jdqG0hXO2rMNct&limit=5").read())
#print json.dumps(data, sort_keys=True, indent=4)


if __name__ == '__main__':
    app.debug = True
    app.run()
