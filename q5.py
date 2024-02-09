def sumOfSquares(n) :
    if n < 0:
        return
    sum = 0
    for i in range(n+1):
        sum += i*i
    return sum

n = int(input('Enter n : '))
sum = sumOfSquares(n)
print(f'Sum : {sum}')

