string1 = "apple orange mango"
string2 = "mango papaya guava"

set1 = set(string1.split())
set2 = set(string2.split())

uncommon_words = set1.symmetric_difference(set2)

print("Uncommon words:", uncommon_words)