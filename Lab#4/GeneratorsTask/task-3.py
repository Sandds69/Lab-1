def twelve(max):
    for i in range(0, max + 1, 12):
        yield i

max = int(input("Enter a number: "))
print(', '.join(str(num) for num in twelve(max)))