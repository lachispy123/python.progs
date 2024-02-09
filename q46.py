string = "hello world"
char_count = {}
for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
least_frequent_char = min(char_count, key=char_count.get)
print("Least frequent character: ", least_frequent_char)