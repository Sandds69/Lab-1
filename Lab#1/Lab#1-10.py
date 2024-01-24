'''
Strings
Strings in python are surrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello".
'''

a = """Vkkaksdksaldkasdkak
dsadkasldaskdalkd
ccdcedaecae мне было лень придумывать но смысл я донёс."""
print(a)

a = '''ДВФЫЛЩЛВЫВЛДЫВЛДФВЛСЬЛФОЫЛЧЯТО
лоылфлыфлчьлфыфчьлфылфылч
фыдфчдфльылфщыл ТУТ тоже самое.'''
print(a)

'''
Строки — это массивы
Как и во многих других популярных языках программирования, строки в Python представляют собой массивы байтов, представляющие символы Юникода.

Однако в Python нет символьного типа данных, один символ — это просто строка длиной 1.

Квадратные скобки можно использовать для доступа к элементам строки.
'''

a = "Hello, World!"
print(a[1])

'''
Цикл по строке
Поскольку строки представляют собой массивы,
мы можем перебирать символы в строке с помощью цикла for.
'''

for x in "banana":
  print(x)

'''
Длина строки
Чтобы получить длину строки, используйте функцию len().
'''
a = "Hello, World!"
print(len(a))

'''
Проверить строку
Чтобы проверить, присутствует ли в строке определенная фраза или символ,
мы можем использовать ключевое слово in.
'''

txt = "The best things in life are free!"
print("free" in txt)

#Используйте его в if заявлении:

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

'''
Чтобы проверить, НЕ присутствует ли определенная фраза или символ в строке,
мы можем использовать ключевое слово not in.
'''

txt = "The best things in life are free!"
print("expensive" not in txt)

#Используйте его в if заявлении:
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")