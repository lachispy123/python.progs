def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def is_strong(n):
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += factorial(digit)
        temp //= 10
    if n == sum:
        return True
    else:
        return False

n = 145
if is_strong(n):
    print(n, "is a Strong number")
else:
    print(n, "is not a Strong number")