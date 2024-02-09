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

n = 153
if is_armstrong(n):
    print(n, "is an Armstrong number")
else:
    print(n, "is not an Armstrong number")
