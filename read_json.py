# Read the json file and categorize data

import json
import pprint
import nltk
import string

file = open("json_file", 'r')

json_data = json.load(file)
d = json.loads(json_data)

pp =pprint.PrettyPrinter(indent=4)

print("Total number of blog articles: ",len(d))

#pp.pprint(d[0])

print(d[0]['title'])
print(d[0]['content'])

def tokenize(content):
    sentences = nltk.sent_tokenize(content)
    stopwords = nltk.corpus.stopwords.words()
    for sentence in sentences:
        words = map(lambda x: nltk.word_tokenize(sentence.lower()))




