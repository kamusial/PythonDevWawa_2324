import os
import re

print('\n 1..................')
for root, dirs, files in os.walk('C:\\Users\\vdi-student\\Desktop\\PythonDevWawa_2324'):
    for filenames in files:
        if 'git' not in root and 'idea' not in root:
            print(root, filenames)
print('\n 2..................')
for root, dirs, files in os.walk('C:\\Users\\vdi-student\\Desktop\\PythonDevWawa_2324'):
    for filenames in files:
        if '.' not in root:
            print(root, filenames)
print('\n 3..................')
for root, dirs, files in os.walk('C:\\Users\\vdi-student\\Desktop\\PythonDevWawa_2324'):
    for filenames in files:
        x = re.search('\.git',root)
        y = re.search('\.idea', root)
        if x is None and y is None:
            print(root, filenames)


