def sum_primes(n):
    sum = 0
    for num in range(2, n+1):
        if is_prime(num):
            sum += num
    return sum

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**(0.5))+1):
        if n % i == 0:
            return False
    return True

n = 20

print("The sum of all prime numbers between 1 and", n, "is:", sum_primes(n))