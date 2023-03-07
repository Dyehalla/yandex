"""
# 2
lst = input().split()
lst = list(map(int, lst))
print(max(lst), lst.count(max(lst)))
# 4
lst = input().split()
for _ in range(int(input())):
    lst.insert(len(lst), lst[0])
    lst.pop(0)
print(*lst)
# 6
print(*input().split()[::3])
# 8
lst = input().split()
my_lst = lst[:]
length = len(lst)
for elem in lst[::-1]:
    if my_lst.count(elem) > 1 or elem == '0':
        my_lst.remove(elem)

print(*my_lst, *[0 for _ in range(len(lst) - len(my_lst))])
"""
# 10
from functools import lru_cache
@lru_cache
def fib(i):
    if i == 1 or i == 2:
        return 1
    return fib(i - 1) + fib(i - 2)


lst = input().split()
fib_lst = [fib(i) for i in range(1, 999)]
flag = True
for elem in lst:
    if int(elem) in fib_lst:
        print(elem, end=' ')
        flag = False
if flag:
    print(0)