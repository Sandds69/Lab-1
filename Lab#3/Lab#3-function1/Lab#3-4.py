def prime(num):
    if(num < 2):
        return False
    else:
        for i in range(2, int(num**0.5) + 1):
            if(num % i == 0):
                return False
        return True
    
def filter_primes(numbers):
    return [num for num in numbers if prime(num)]

print(filter_primes((1, 2, 3, 4, 5)))