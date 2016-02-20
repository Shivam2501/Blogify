# Read the json file and categorize data

import json
import pprint
import nltk

file = open("json_file2", 'r')

json_data = json.load(file)
d = json.loads(json_data)

pp =pprint.PrettyPrinter(indent=4)

print("Total number of blog articles: ",len(d))

#pp.pprint(d[0])

print(d[0]['title'])

