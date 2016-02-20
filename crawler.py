import urllib.request
import urllib.response

from bs4 import BeautifulSoup
from datetime import date,timedelta

# Collect all the links of the articles in the last 30 days of reuters.com

for i in range(30):
    d=date.today()- timedelta(days=i)
    curr_date=d.strftime("%m%d%Y")

    #print(curr_date)
    req_url = urllib.request.Request("http://www.reuters.com/news/archive?date="+curr_date)
    html_data = None

    #print(req_url)

    with urllib.request.urlopen(req_url) as html:
        html_data = html.read()

    soup = BeautifulSoup(html_data, 'html.parser')

    links = []

    for link in soup.find_all('a'):
        links.append(link.get('href'))

    article = "/article"
    file = open("link_file", 'a')

    for i in range(len(links)):
        if article in str(links[i]):
            file.write(links[i]+ "\n")


file.close()

