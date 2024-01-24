#Python - Format - Strings

'''
String Format
As we learned in the Python Variables chapter,
we cannot combine strings and numbers like this:
age = 36
txt = "My name is John, I am " + age
print(txt)

Но мы можем комбинировать строки и числа, используя этот format()метод!

Метод format()принимает переданные аргументы,
форматирует их и помещает в строку, где {}находятся заполнители:
'''
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
