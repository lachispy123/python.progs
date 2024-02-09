string = "hello world, world is a beautiful place"
words = string.split()

replaced_string = " ".join([word if words.count(word) == 1 else "DUPLICATE" for word in words])

print("Original string:", string)
print("Replaced string:", replaced_string)
