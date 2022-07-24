import sys

input = sys.stdin.readline

N = int(input().rstrip())
arr = [[] for _ in range(N)]

for i in range(N):
    arr[i] = list(map(int, input().split()))

max_count = 0


def dfs(di1, di2, di1_index, count):
    global max_count
    if max_count < count:
        max_count = count

    if di1_index == 2*N:
        return

    for di2_index in range(2*N):

        if (di1_index + di2_index - N) % 2 == 1:
            continue
        if (di1_index - di2_index + N) % 2 == 1:
            continue
        i = (di1_index + di2_index - N) // 2
        j = (di1_index - di2_index + N) // 2

        if not (0 <= i < N and 0 <= j < N):
            continue
        if arr[i][j] == 0:
            continue

        if not di2[di2_index] and not di1[di1_index]:
            di1[di1_index] = di2[di2_index] = True
            count += 1
            dfs(di1, di2, di1_index + 1, count)
            count -= 1
            di1[di1_index] = di2[di2_index] = False
    dfs(di1, di2, di1_index + 1, count)


dfs([False for _ in range(2 * N)], [False for _ in range(2 * N)], 0, 0)

print(max_count)
