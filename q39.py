def contains_all_vowels(string):
    vowels = set('aeiou')
    return vowels.issubset(string.lower())

string1 = "The quick brown fox jumps over the lazy dog"
string2 = "The quick brown fox jumps over the laziest dog"

print(contains_all_vowels(string1))
print(contains_all_vowels(string2))