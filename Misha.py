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
        another_words[keys.index(sorted(list(i)))].append(i)

for i in another_words:
    sorted(i)
    print(*i)'''


def tribonacci(n):
    if 0 <= n <= 1:
        return 0
    elif 2 <= n <= 3:
        return 1
    else:
        return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)
