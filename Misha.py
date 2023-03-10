'''words = []
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
        another_words[keys.index(sorted(list(i)))].append(i)j

for i in another_words:
    sorted(i)
    print(*i)'''

import pymorphy2
from sys import stdin


def pls_return_stripped_word(word):
    output = ''
    for letter in word:
        if letter.isalpha():
            output = output + letter
    return output.lower()


user_input = [i for i in stdin]
found = []
nouns = []
morph = pymorphy2.MorphAnalyzer()
for sentence in user_input:
    for word in sentence.split():
        for variant in morph.parse(pls_return_stripped_word(word)):
            if variant.score > 0.5 and variant.tag.POS == "NOUN":
                if variant.normal_form not in found:
                    found.append(variant.normal_form)
                    nouns.append([variant.normal_form, 1])
                    break
                else:
                    nouns[found.index(variant.normal_form)][1] += 1
                    break
nouns.sort(key=(lambda x: (x[1], x[0])), reverse=True)
for words in nouns[:10]:
    print(words[0], end=" ")