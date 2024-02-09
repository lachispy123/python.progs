def is_substring(s, sub):
    return sub in s

string = input("Enter a string: ")
substring = input("Enter a substring: ")
if is_substring(string, substring):
    print(f"{substring} is present in {string}.")
else:
    print(f"{substring} is not present in {string}.")