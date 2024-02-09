string = "The quick brown fox jumps over the lazy dog"
words = string.split()

for word in words:
    if len(word) % 2 == 0:
        print(word)
