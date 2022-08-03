import sys
input = sys.stdin.readline

n = int(input())

dot = []

for _ in range(n):
    x, y = map(int, input().split())
    dot.append((x,y))

total = 0
for i in range(n):
    total += dot[i][0] * dot[(i+1)%n][1]
    total -= dot[i][0] * dot[(i+n-1)%n][1]
print(f"{abs(total/2):.1f}")