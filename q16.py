num = int(input("Enter a number: "))
product_of_digits = 1
while num > 0:
    product_of_digits *= num % 10
    num //= 10
print("Product of digits:", product_of_digits)