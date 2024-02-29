import re

with open('sample.txt', 'r', encoding='utf-8') as file:
    check = file.read()

first = re.findall(r'\w*ab*\w*', check)
print(first)

second = re.findall(r'\w*ab{2,3}\w*', check)
print("\n", second)

third = re.findall(r'[a-z]+_[a-z]+', check)
print("\n", third)

fourth = re.findall(r'[A-Z][a-z]*', check)
print("\n", fourth)

fifth = re.findall(r'[\w-]*a\w*b', check)
print("\n", fifth)

sixth = re.sub(r'[ ,.]', ':', check)
print("\n", sixth)