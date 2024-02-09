string = input("Enter a string: ")
word_count = Counter(string.split())
print("Word frequency:")
for word, count in word_count.items():
    print(f"{word}: {count}")