import os
import time
from pathlib import Path

print(os.getcwd())
os.chdir(r'C:\Users\vdi-student\Desktop')
print(os.getcwd())
time.sleep(1)
os.mkdir('Folder1')
time.sleep(1)
os.rename('Folder1', 'Folder2')
time.sleep(1)
os.rmdir('Folder2')
os.chdir((Path.home()))
print(os.getcwd())

os.system('cmd /c "cd C:\\Users\\vdi-student\\Desktop && ipconfig /all > result.txt"')
