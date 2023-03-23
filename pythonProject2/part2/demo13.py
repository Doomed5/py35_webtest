import os
import time

os.chdir('stadic')
dir = os.getcwd()
print(dir)
# os.mkdir('images')
# os.mkdir('images/avatar')
# os.chdir('./images')
# os.chdir('avatar')
# os.chdir('../')
# os.chdir('../')
os.mkdir('test')

print(os.listdir())
time.sleep(20)
os.rmdir('test')
dir = os.getcwd()
print(dir)