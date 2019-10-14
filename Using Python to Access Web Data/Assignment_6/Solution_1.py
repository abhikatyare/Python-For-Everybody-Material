# Author    : Abhishek Katyare
# Date      : 14th October, 2019

import urllib.error, urllib.error, urllib.request
import json

# Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_219911.json (Sum ends with 96)

# data = ''' [
#     {
#       "name": "Matthias",
#       "count": 97
#     },
#     {
#       "name": "Geomer",
#       "count": 97
#     }
#   ]    '''

url = input('Enter -')
dt = urllib.request.urlopen(url)
data = dt.read()
input_data = json.loads(data)

print(sum([data['count'] for data in input_data['comments']]))