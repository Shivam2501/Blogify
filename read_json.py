# Read the json file and categorize data

import json
import pprint
import nltk
import string
import re
import operator
import math

file = open("json_file", 'r')

json_data = json.load(file)
d = json.loads(json_data)

pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(d[0])

print("Total number of blog articles: ", len(d))

training_dataset = []
for i in range(5):
    training_dataset.append(d[i])


def remove_punctuation(word):
    return word if str(word) not in string.punctuation else None


def remove_duplicates(words):
    filter_d = []
    for i in words:
        if i not in filter_d:
            filter_d.append(i)
    return filter_d


def tokenize(content):
    sentences = nltk.word_tokenize(content)
    stopwords = nltk.corpus.stopwords.words()
    words = map(lambda x: x if x not in stopwords else None, sentences)
    words_filtered = []
    for word in words:
        words_filtered.append(remove_punctuation(word))
    words_filtered = map(lambda x: x if len(str(x)) > 2 else None, words_filtered)
    words_filtered = filter(None, words_filtered)
    words_filtered = remove_duplicates(words_filtered)
    return words_filtered


def frequency(content):
    words = nltk.word_tokenize(content)
    freq = nltk.FreqDist(words)
    return freq


def filter_freq(freq, word):
    return freq[word]


def word_count(content):
    r = re.compile(r'[{}]'.format(string.punctuation))
    new_strs = r.sub(' ', content)
    word_count = len(new_strs.split())
    return word_count


def word_freq(word, content):
    word_filter = tokenize(content)
    word_freq = frequency(content)
    count = filter_freq(word_freq, word)
    return count


def tf(word, content):
    count = word_freq(word, content)
    total_word_count = word_count(content)
    return count / total_word_count


def number_containing(word, data):
    count = 0
    for i in range(len(data)):
        if word_freq(word, data[i]['content']) > 0:
            count += 1
    return count


def idf(word, data):
    return math.log(len(data) / (1 + number_containing(word, data)))


def tfidf(word, content, data):
    return tf(word, content) * idf(word, data)

word_filter = tokenize(training_dataset[0]['content'])
tf_scores = {word: tfidf(word, training_dataset[0]['content'], training_dataset) for word in word_filter}
sorted_tfscores = sorted(tf_scores.items(), key=operator.itemgetter(1), reverse=True)
for key, value in sorted_tfscores:
    print(key, value)
