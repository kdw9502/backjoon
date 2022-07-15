import sys
input = sys.stdin.readline
n = int(input())
l = set()
sum = 0
for _ in range(n):
    k = int(input())
    for count, val in set(l):
        if count < n // 2:
            l.add((count + 1, k + val))
    l.add((1,k))
    sum += k
min_diff = 45000
min_index = -1
l = list(l)
for i, (count, _sum) in enumerate(l):
    if count != n//2:
        continue
    diff = abs(_sum - sum / 2)
    if diff < min_diff:
        min_diff = diff
        min_index = i
a = l[min_index][1]
b = sum - a

if a > b:
    print(b)
    print(a)
else:
    print(a)
    print(b)
