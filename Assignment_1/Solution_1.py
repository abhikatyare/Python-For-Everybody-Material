import re

FILE_PATH = r"C:\Users\v-abkaty\Desktop\Workspace\Python_Course\Assignment_1\actual_data.txt"
FILE_DATA = open(FILE_PATH,"r+")

print( sum([int(x) for x in re.findall(r'[0-9]+',FILE_DATA.read())]))