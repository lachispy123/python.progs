string1 = "hello world"
string2 = "hola mundo"
count = 0
for i in range(len(string1)):
    if string1[i] == string2[i]:
        count += 1
print("Number of matching characters: ", count)