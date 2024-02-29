def decline(n):
    for i in range(n, -1, -1):
        yield i

n = int(input("Enter a number: "))
print(', '.join(str(num) for num in decline(n)))