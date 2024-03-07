first = open("sample.txt", "r")
second = open("txtfile.txt", "a")
second.write(first.read())