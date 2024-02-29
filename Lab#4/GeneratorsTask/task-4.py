def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
print(', '.join(str(num) for num in squares(a, b)))