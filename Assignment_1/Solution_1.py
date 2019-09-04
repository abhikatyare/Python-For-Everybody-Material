import re

x = "From: v-abkaty@microsoft.com"
y = re.findall(r'^From: (\S+@\S+)',x)
print(y)