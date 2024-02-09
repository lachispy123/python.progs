string = "Hello, world!"

char_count = {}
for char in string:
    char_count[char] = char_count.get(char, 0) + 1
new_string = ''.join(char_count.keys())
print(new_string)