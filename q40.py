string1 = "Hello, world!"
string2 = "Holly, Molly!"

count = 0
for char1, char2 in zip(string1, string2):
    if char1 == char2:
        count += 1

print(count)