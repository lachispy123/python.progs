def print_primes(n):
    primes = []
    for num in range(2, n+1):
        if is_prime(num):
            primes.append(num)
    return primes

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**(0.5))+1):
        if n % i == 0:
            return False
    return True

n = 20