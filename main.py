"""
# 1
input()
print(*sorted(input().split(), key=lambda num: (int(num) % 10, int(num))))

# 3
import statistics
print(statistics.median(map(int, input().split())))

# 5

lst = input().split()
print(*sorted(map(int, lst)))
print(len(set(lst)))

# 7
lst = input().split()
k, m, d = map(int, input().split())
res = lst[:k] + list(map(str, sorted(map(int, lst[k:m + 1]))[::d])) + lst[m + 1:]
print(*res)
"""

# 9
lst = list(map(int, input().split()))

while True:
    if not lst:
        print(-1)
        break
    i = max(lst)
    if lst.count(i) > 1:
        print(i)
        break
    else:
        lst.remove(i)