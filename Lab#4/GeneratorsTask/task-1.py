def squares(max):
    count = 1
    while(count <= max):
        yield count * count
        count += 1

max = int(input("Input max number: "))
counter = squares(max)
for i in range(1, max + 1):
    print(next(counter))