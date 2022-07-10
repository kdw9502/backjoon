import sys

input = sys.stdin.readline

N, val = map(int, input().split())
coins = []
for i in range(N):
    coins.append(int(input()))

count = 0
coins.reverse()
for coin in coins:
    count += val // coin
    val = val % coin
    if val == 0:
        break
print(count)