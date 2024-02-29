def even(max):
    for i in range(max + 1):
        if (i % 2 == 0):
            yield i

max = int(input("Input a number: "))
print(', '.join(str(num) for num in even(max)))