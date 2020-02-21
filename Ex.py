# Programme to find the maximum repeated character into a string.
sentence = "This is a common interview question"

char_count = {}
for char in sentence:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(char_count)
char_count_sorted = sorted(char_count.items(), key=lambda kv: kv[1], reverse=True)
print("Maximum repeated character is ", char_count_sorted[1])
