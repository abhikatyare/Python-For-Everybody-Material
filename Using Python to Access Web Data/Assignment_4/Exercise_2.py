# Author : Abhishek Katyare
# Date   : 5th September, 2019

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter URL -')
fileHandler = urllib.request.urlopen(url)
data = BeautifulSoup(fileHandler, 'html.parser')

tags = data('a')
for tag in tags:
    print(tag.get('href',None))