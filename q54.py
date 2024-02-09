string = "hello world"
duplicates = []

for char in set(string):
    if string.count(char) > 1:
        duplicates.append(char)

print("Duplicate characters:", duplicates)
