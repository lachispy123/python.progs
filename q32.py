def reverse_words(s):
    words = s.split()
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)

string = input("Enter a string: ")
reversed_string = reverse_words(string)
print(f"Reversed string: {reversed_string}")