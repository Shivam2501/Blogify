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
def remove_punctuation(word):
    return word if str(word) not in string.punctuation else None

def remove_duplicates(words):
    filter = []
    for i in words:
        if i not in filter:
            filter.append(i)
    return filter

def tokenize(content):
    sentences = nltk.word_tokenize(content)
    stopwords = nltk.corpus.stopwords.words()
    words = map(lambda x: x if x not in stopwords else None, sentences)
    words_filtered = []
    for word in words:
        words_filtered.append(remove_punctuation(word))
    words_filtered = map(lambda x: x if len(str(x))>2 else None, words_filtered)
    words_filtered = filter(None, words_filtered)
    words_filtered = remove_duplicates(words_filtered)
    return words_filtered

def frequency(content):
    words = nltk.word_tokenize(content)
    freq = nltk.FreqDist(words)
    return freq

def filter_freq(freq,word):
    return freq[word]

print(d[0]['title'])
word_filter = tokenize(d[0]['content'])
word_freq = frequency(d[0]['content'])
for word in word_filter:
    print(word,filter_freq(word_freq,word))


