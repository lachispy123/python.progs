def is_perfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    if sum == n:
        return True
    else:
        return False

n = 28
if is_perfect(n):
    print(n, "is a Perfect number")
else:
    print(n, "is not a Perfect number")