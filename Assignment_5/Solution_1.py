# Author    : Abhishek Katyare
# Date      : 16th September, 2019

import xml.etree.ElementTree as ET

# Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_219910.xml (Sum ends with 86)

input = '''<comment>
  <name>Matthias</name>
  <count>97</count>
</comment>'''


data = ET.fromstring(input)

print(data.findtext('name'))
print(data.findtext('count'))