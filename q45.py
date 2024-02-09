string = "hello world"
new_string = ""
for char in string:
    if char not in new_string:
        new_string += char
print(new_string)
