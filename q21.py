def hcf(a, b):
    if b == 0:
        return a
    else:
        return hcf(b, a % b)

num1 = 10
num2 = 20

print("The HCF of", num1, "and", num2, "is", hcf(num1, num2))