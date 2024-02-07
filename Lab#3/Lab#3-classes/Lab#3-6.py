def prime(num):
    if(num < 2):
        return False
    else:
        for i in range(2, int(num**0.5) + 1):
            if(num % i == 0):
                return False
        return True
    
def filter_primes(numbers):
    primeFilter = filter(lambda num : prime(num), numbers)
    return list(primeFilter)

#Lambda 