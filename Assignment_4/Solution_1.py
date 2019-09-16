# Author : Abhishek Katyare
# Date   : 9th September, 2019

import urllib.parse, urllib.request, urllib.error
from bs4 import BeautifulSoup
import re

##  Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
##  Actual data: http://py4e-data.dr-chuck.net/comments_219908.html (Sum ends with 32)

url = input('Enter -')
data = urllib.request.urlopen(url)
obj = BeautifulSoup(data,'html.parser')

temp=0
tags = obj('span')
for tag in tags:
   temp += sum([int(x) for x in re.findall('>(.+)<',tag.decode())])

print(temp)