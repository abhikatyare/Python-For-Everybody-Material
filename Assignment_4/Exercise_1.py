# Author : Abhishek Katyare
# Date   : 5th September, 2019

import urllib.request, urllib.parse, urllib.error

fileHandler = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")

for line in fileHandler:
    print(line.decode())