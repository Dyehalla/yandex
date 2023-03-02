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
'''
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
'''
# Первая
print([int(i) for i in input().split()].count(int(input())))

# Третья
oleg = [int(i) for i in input().split()]
oleg.reverse()
print(*oleg)

# пятая

pre_zero, post_zero, zeros = [], [], []
initial = [int(i) for i in input().split()]
for i in initial:
    if i > 0:
        pre_zero.append(i)
    elif i < 0:
        post_zero.append(i)
    elif i == 0:
        zeros.append(i)
pre_zero.sort()
print(*pre_zero, *zeros, *post_zero)

# Седьмая

oleg = [int(i) for i in input().split()]
oleg.sort()
print(*oleg[0:3])

# Девятая

output = []
oleg = [int(i) for i in input().split()]
div, div_not = map(int, input().split())
for i in oleg:
    if i % div == 0 and i % div_not != 0 and len(str(i)) == 3:
        output.append(i)
if output == []:
    print(0)
else:
    print(*output)