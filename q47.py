string = "hello world"
max_freq_char = max(set(string), key = string.count)
print("Maximum frequency character:", max_freq_char)