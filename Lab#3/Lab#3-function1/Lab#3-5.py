from itertools import permutations

def allPermutations(str):
    for s in permutations(str):
        print(''.join(s))