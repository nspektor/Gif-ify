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
giphyUrl = "https://api.giphy.com/v1/gifs/translate"
#n0 = ""
#word = ""
g0 = ""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/category/')
def category():
    return render_template('category.html')

@app.route('/category/<name>')
def categoryName(name):
    subject = name.capitalize()
    #print(subject)
    ans = getUrl(subject)
    #words = []
    #resultURLs = []

    #for i in range(len(urls)):
        #print(urls[i] + " " + keywords[i])
        #splitHead = keywords[i].split(' ')
        #word = splitHead[0]
        #words.append(word)
    #s=word
    ansarr = ans.split(' ')
    word = ansarr[0]
    n0 = ansarr[1]
    print(word + 'ABOUT TO FIND GIF')
    querystring = {"api_key":"TN5SAJ5tC9a68o8fm1jdqG0hXO2rMNct","s":word}

    response = requests.request("GET", giphyUrl, params=querystring)
    jsonR = response.json()
    data = json.dumps(jsonR)
    parsed_json = json.loads(data)
    print(parsed_json["data"])
    g0 = parsed_json["data"]["embed_url"]

    return render_template('category.html', g0=g0, n0=n0)


def getUrl(subject):
    articles = api.search( fq='The New York Times', begin_date='20171010', fl='web_url, section_name, headline', facet_field='section_name')
    data = json.dumps(articles)
    parsed_json = json.loads(data)
    i = 0
    word = "Trump"
    n0 = "https://www.nytimes.com/2017/10/12/opinion/ivana-ivanka-trump-book.html"
    while i < len(parsed_json["response"]["docs"]) :
        result = parsed_json["response"]["docs"][i]
        print(i)
        print(result['section_name'])
        #print(result["section_name"])
        if(result["section_name"] == subject):
            #urls.append(result['web_url'])
            n0 = result['web_url']
            title = result['headline']['main']
            print(title)
            warr = title.split(' ')
            word = warr[0]
            print(word)
            break
            #keywords.append(result['headline']['main'])
            #print("ADDED")
        i += 1

    return word + " " + n0



data = json.loads(urllib.urlopen("http://api.giphy.com/v1/gifs/search?q=ryan+gosling&api_key=TN5SAJ5tC9a68o8fm1jdqG0hXO2rMNct&limit=5").read())
#print json.dumps(data, sort_keys=True, indent=4)


if __name__ == '__main__':
    app.debug = True
    app.run()
