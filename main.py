words_amount = int(input())
words = list()
result = list()
for _ in range(words_amount):
    words.append(input().lower())

for word1 in words:
    first_word = True
    for word2 in words:
        if words.index(word1) != words.index(word2):
            if sorted(list(word1)) == sorted(list(word2)):
                if first_word:
                    result.append([word1, word2])
                    first_word = False
                    index = len(result) - 1
                else:
                    result[index].append(word2)
        if not first_word:
            result[index].sort()
    for i in result[index]:
        words.remove(i)


for res in sorted(result, key=lambda lst: lst[0]):
    print(*res)