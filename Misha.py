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


def is_hypersimple(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


number = int(input())
while (number != 0):
    if is_hypersimple(number):
        number //= 10
    else:
        print("NO")
        break
else:
    print("YES")
