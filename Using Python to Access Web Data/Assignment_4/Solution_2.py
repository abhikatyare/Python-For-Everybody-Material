# Author : Abhishek Katyare
# Date   : 9th September, 2019

import urllib.parse, urllib.request, urllib.error
from bs4 import BeautifulSoup
import re

##  Sample data: http://py4e-data.dr-chuck.net/known_by_Fikret.html (Last name is Anayah)
##  Actual data: http://py4e-data.dr-chuck.net/known_by_Taya.html (name ends with L)

url = input('Enter -')
count = int(input('Enter the Count -'))
position = int(input('Enter the Position -'))


for x in range(count):
   data = urllib.request.urlopen(url)
   obj = BeautifulSoup(data,'html.parser')

   tags = obj('a')
   url = tags[position-1].get('href',None)
   print(tags[position-1].get_text())


