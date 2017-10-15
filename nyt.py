from nytimesarticle import articleAPI
import json
from pprint import pprint
api = articleAPI('28bba9543b494e2f9d15976a0fa44f5c')
articles = api.search( fq='The New York Times', begin_date='20171010', fl='web_url', sort='newest', facet_field='subject=Sports', facet_filter='true')
data = json.dumps(articles)
parsed_json = json.loads(data)
pprint(parsed_json)
for i in range(0,6):
    print(parsed_json["response"]["docs"][i]["web_url"])
