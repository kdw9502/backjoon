import sys

input = sys.stdin.readline

n = int(input())
xs = []
ys = []
zs = []
xyzs = []

dist = [0 for i in range(n)]
selected = [0 for i in range(n)]
for i in range(n):
    x, y, z = map(int, input().split())
    xyzs.append((x,y,z))

arr = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    queue = []


