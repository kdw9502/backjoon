import sys

input = sys.stdin.readline

def ans(a, b):
    cycle = [[0],[1],[2,4,8,6],[3,9,7,1],[4,6],[5],[6],[7,9,3,1],[8,4,2,6],[9,1]]
    a = a % 10
    cycle = cycle[a]
    b = (b + len(cycle) -1) % len(cycle)
    sol = cycle[b]
    if sol == 0:
        print(10)
    else:
        print(cycle[b])

n= int(input())
for i in range(n):
    a, b = map(int, input().split())
    ans(a,b)

