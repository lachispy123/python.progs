def lcm(a, b):
    hcf = find_hcf(a, b)
    return (a*b)//hcf

def find_hcf(x, y):
    while(y):
        x, y = y, x % y
    return x

num1 = 10
num2 = 20

print("The LCM of", num1, "and", num2, "is", lcm(num1, num2))