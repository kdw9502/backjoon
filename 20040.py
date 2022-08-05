import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, m = map(int, input().split())

root = [i for i in range(n)]


def find(x):
    if root[x] == x:
        return x
    root[x] = find(root[x])
    return root[x]


def union(x, y):
    a = find(y)
    b = find(x)
    if a < b:
        a,b = b,a
    root[a] = b



for i in range(m):
    a, b = map(int, input().split())

    if find(a) == find(b):
        print(i + 1)
        found = True
        break
    union(a, b)
else:
    print(0)