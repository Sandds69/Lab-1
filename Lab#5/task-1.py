import re

with open('sample.txt', 'r', encoding='utf-8') as file:
    check = file.read()

def camelCase(match):
    words = match.group()
    return words.split('_')[0] + ''.join(x.capitalize() for x in words.split('_')[1:])

ans = re.sub(r'[a-z]+_[a-z]+', camelCase , check)
print(ans)
