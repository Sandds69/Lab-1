def reverseWords(str):
    li = str.split(" ")
    li.reverse()
    return ' '.join(li)

print(reverseWords("We are ready"))