def is_armstrong(n):
    sum = 0
    order = len(str(n))
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    if n == sum:
        return True
    else:
        return False

n = 1000
print("Armstrong numbers between 1 and", n, "are:")
for i in range(1, n+1):
    if is_armstrong(i):
        print(i)