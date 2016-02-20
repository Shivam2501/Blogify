# Read the json file and categorize data

import json
import pprint

file = open("json_file", 'r')

json_data = json.load(file)
d = json.loads(json_data)

pp =pprint.PrettyPrinter(indent=4)

print("Total number of blog articles: ",len(d))

#pp.pprint(d[0])





