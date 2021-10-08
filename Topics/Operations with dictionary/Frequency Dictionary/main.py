# put your python code here
words = input().split()
word_map = {}

for word in words:
    word = word.lower()
    if word not in word_map:
        word_map[word] = 1
    else:
        word_map[word] += 1

for key, value in word_map.items():
    print(key, value)
