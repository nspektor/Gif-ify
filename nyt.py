from nytimesarticle import articleAPI
import json
from pprint import pprint
api = articleAPI('7adeb932f30043dea8bd262313d00d3c')
articles = api.search( fq='The New York Times', begin_date='20171010', fl='web_url, section_name', sort='newest', facet_field='section_name', facet_filter='true')
data = json.dumps(articles)
parsed_json = json.loads(data)
pprint(parsed_json)
counter = 0
for i in range(0,10):
    if(counter < 6):
        result = parsed_json["response"]["docs"][i]
    #print(result["section_name"])
        if(result["section_name"] == "Sports"):
            counter+=1
            print(result["web_url"])
    else:
        break
