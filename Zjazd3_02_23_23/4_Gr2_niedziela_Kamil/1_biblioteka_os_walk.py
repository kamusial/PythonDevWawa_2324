import os
import re

for root, dirs, files in os.walk('C:\\Users\\vdi-student\\Desktop\\PythonDevWawa_2324'):
    for filenames in files:
        if 'git' not in root and 'idea' not in root:
            print(root, filenames)

for root, dirs, files in os.walk('C:\\Users\\vdi-student\\Desktop\\PythonDevWawa_2324'):
    for filenames in files:
        if '.' not in root:
            print(root, filenames)