#word frequency counter
def count_words(text):
    words = text.lower().split()
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

text = input("Enter a sentence or paragraph: ")
frequencies = count_words(text)

print("Word Frequencies:")
for word, count in frequencies.items():
    print(f"{word}: {count}")
