import re

with open('sample.txt', 'r', encoding='utf-8') as file:
    check = file.read()

print(re.findall(r'\b[a-z]+(?:[A-Z][a-z]*)+\b', check))