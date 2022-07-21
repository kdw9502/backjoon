import sys

input = sys.stdin.readline
n, m = map(int, input().split())
required = [0 for _ in range(n+1)]
required[0] = n
left = [[] for _ in range(n+1)]
right = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    required[b] += 1
    left[b].append(a)
    right[a].append(b)
queue = []
remain = n
done = set()
while remain:
    for i in range(n + 1):
        if required[i] == 0 and i not in done:
            print(i, end=" ")
            queue.append(i)
            done.add(i)
            remain -= 1
    while queue:
        j = queue.pop(0)
        for _right in right[j]:
            required[_right] -= 1
