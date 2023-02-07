words = []
keys = []
another_words = []
result = []
for n in range(int(input())):
    words.append(input().lower())
for i in words:
    if sorted(list(i)) in keys:
        another_words[keys.index(sorted(list(i)))].append(i)
    else:
        keys.append(sorted(list(i)))
        another_words.append([])
        another_words[keys.index(sorted(list(i)))].append(i)

for i in another_words:
    sorted(i)
    print(*i)