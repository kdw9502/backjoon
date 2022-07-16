import sys

input = sys.stdin.readline

N = int(input().rstrip())

def dfs(y, di1, di2, i):
    count = 0
    if i == N:
        count += 1
    for j in range(N):
        if not y[j] and not di1[i-j+N] and not di2[i+j]:
            y[j] = di1[N + i - j] = di2[i + j] = True
            count += dfs(y, di1, di2, i + 1)
            y[j] = di1[N + i - j] = di2[i + j] = False
    return count


count = dfs([False for _ in range(N)], [False for _ in range(2 * N)], [False for _ in range(2 * N)], 0)

print(count)
