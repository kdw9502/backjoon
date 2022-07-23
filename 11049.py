import sys

input = sys.stdin.readline

n = int(input())
l = []
for i in range(n):
    a, b = map(int, input().split())
    l.append((a, b))
