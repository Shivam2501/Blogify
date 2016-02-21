# Parse all the links from link_file and create a json file with all the scraped data

import urllib.request
import urllib.response
import json

from bs4 import BeautifulSoup

file = open("link_file", 'r')

content = file.readlines()

data_array = []
#print(len(content))

for i in range(len(content)):
    print("Blog: ",i)
    req_url = urllib.request.Request("http://reuters.com"+content[i])
    html_data = None

    with urllib.request.urlopen(req_url) as html:
        html_data = html.read()

    soup = BeautifulSoup(html_data, 'html.parser')

    data = {}

    data['link'] = "http://reuters.com"+content[i]
    data['id'] = i

    for heading in soup.find_all(class_="article-headline"):
        #print(heading.text)
        data['title'] = heading.text

    for timestamp in soup.find_all(class_="timestamp"):
        #print(timestamp.text)
        data['timestamp'] = timestamp.text

    for author in soup.find_all(class_="byline"):
        #print(author.text)
        data['author'] = author.text

    for location in soup.find_all(class_="location"):
        #print(location.text)
        data['location'] = location.text

    for article in soup.find_all(id="articleText"):
        #print(article.text)
        data['content'] = article.text

    tags = []
    for related_tags in soup.find_all(class_="related-topics"):
        for child in related_tags.find_all('a'):
            #print(child.text)
            tags.append(child.text)

    data['tags'] = tags

    data_array.append(data)


json_data = json.dumps(data_array)

file.close()
file = open("json_file", 'w')
json.dump(json_data, file)
file.close()
