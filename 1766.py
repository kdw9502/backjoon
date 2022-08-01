n, m = map(int, input().split())

vertices = [set() for _ in range(n+1)]
link = [set() for _ in range(n+1)]
history = [0 for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    vertices[b].add(a)
    link[a].add(b)
result = []
queue = []
while len(result) < n:
    for i in range(1, n+1):
        if len(vertices[i]) == 0 and history[i] == 0:
            result.append(i)
            history[i] = 1
            for j in link[i]:
                if i in vertices[j]:
                    vertices[j].remove(i)
            break

print(*result, sep=" ")