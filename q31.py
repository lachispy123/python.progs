def is_palindrome(s):
    return s == s[::-1]

def is_symmetrical(s):
    n = len(s)
    for i in range(n//2):
        if s[i] != s[n-i-1]:
            return False
    return True

string = input("Enter a string: ")
if is_palindrome(string):
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a palindrome.")

if is_symmetrical(string):
    print(f"{string} is symmetrical.")
else:
    print(f"{string} is not symmetrical.")
