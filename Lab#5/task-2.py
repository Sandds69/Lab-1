import re

with open('sample.txt', 'r', encoding='utf-8') as file:
    check = file.read()

print(re.split(r'[A-Z]+', check))