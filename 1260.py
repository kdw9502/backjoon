from collections import defaultdict

e_v_set = defaultdict(set)
e_v = defaultdict(list)
n, m, v = map(int, input().split())
for i in range(m):
    e1, e2 = map(int, input().split())
    e_v_set[e1].add(e2)
    e_v_set[e2].add(e1)
for key, val in e_v_set.items():
    e_v[key] = sorted(val)


def dfs(history, current):
    print(current, end=" ")
    history.append(current)
    if len(history) == len(e_v):
        return
    for next in e_v[current]:
        if next not in history:
            dfs(history, next)


def bfs(start):
    history = [start]
    queue = [start]
    print(start, end=" ")
    while True:
        val = queue.pop(0)
        for e in e_v[val]:
            if e in history:
                continue
            queue.append(e)
            history.append(e)
            print(e, end=" ")
        if len(history) == len(e_v) or not queue:
            return


def main():
    dfs([], v)
    print()
    bfs(v)
    print()

main()
