import sys
sys.setrecursionlimit(50000)


input = sys.stdin.readline


def dfs(history, arr,y,x,n,m):
    if history[y][x]:
        return
    if not arr[y][x]:
        return
    history[y][x] = 1
    if y > 0:
        dfs(history,arr,y-1,x,n,m)
    if y < n-1:
        dfs(history,arr, y +1, x, n, m)
    if x > 0:
        dfs(history,arr,y,x-1,n,m)
    if x < m-1:
        dfs(history,arr, y, x +1, n, m)


t = int(input())
for _ in range(t):
    m,n,k = map(int, input().split())

    count = 0
    arr = [[0 for _ in range(m)] for _ in range(n)]
    history = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1

    for y in range(n):
        for x in range(m):
            if arr[y][x] == 1 and history[y][x] == 0:
                dfs(history, arr, y,x,n,m)
                count += 1
    print(count)
