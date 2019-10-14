# Author    : Abhishek Katyare
# Date      : 14th October, 2019

import urllib.parse, urllib.error, urllib.request
import json

serviceUrl = "http://py4e-data.dr-chuck.net/json?"

location = input("Enter Location : ")
arr = dict()
arr['address'] = location
arr['key'] = 42
url = serviceUrl + urllib.parse.urlencode(arr)
print(url)
dt = urllib.request.urlopen(url)
data = dt.read()
input_data = json.loads(data)
print(input_data['results'][0]["place_id"])