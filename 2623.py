import sys
input = sys.stdin.readline

n, m = map(int, input().split())

history = [1] * (n+1)
history[0] = 0
need = [set() for _ in range(n + 1)]
link = [set() for _ in range(n + 1)]

for i in range(m):
    order = list(map(int, input().split()))[1:]
    for list_index in range(len(order)-1):
        need[order[list_index + 1]].add(order[list_index])
        link[order[list_index]].add(order[list_index + 1])

result = []

for _ in range(n):
    for i in range(1, n+1):
        if not need[i] and history[i]:
            result.append(i)
            history[i] = 0
            for index in link[i]:
                need[index].remove(i)

if len(result) < n:
    print(0)
else:
    print(*result, sep="\n")
