def remove_char(s, i):
    return "".join([s[j] for j in range(len(s)) if j != i])

string = input("Enter a string: ")
i = int(input("Enter the index of the character to be removed: "))
new_string = remove_char(string, i)
print(f"New string: {new_string}")
