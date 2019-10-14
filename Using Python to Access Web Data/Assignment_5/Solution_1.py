# Author    : Abhishek Katyare
# Date      : 14th October, 2019

import urllib.error, urllib.parse, urllib.request
import xml.etree.ElementTree as ET

# Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_219910.xml (Sum ends with 86)

# input = '''<comment>
#             <name>Matthias</name>
#             <count>97</count>
#            </comment>
#            <comment>
#             <name>Alies</name>
#             <count>72</count>
#            </comment>
#           '''

url = input('Enter -')
dt = urllib.request.urlopen(url)
data = dt.read()
input_data = ET.fromstring(data)
counts = input_data.findall(".//count")
print(sum([int(count.text) for count in counts]))