def snake_to_pascal(s):
    words = s.split("_")
    return "".join(word.capitalize() for word in words)

string = input("Enter a string in snake_case format: ")
pascal_string = snake_to_pascal(string)
print(f"Pascal case string: {pascal_string}")