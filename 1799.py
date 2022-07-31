import sys

input = sys.stdin.readline

N = int(input().rstrip())
arr = [[] for _ in range(N)]

for i in range(N):
    arr[i] = list(map(int, input().split()))

max_count = 0


def dfs(di1_index, color, count):
    global max_count, dia1, dia2
    if max_count < count:
        max_count = count

    if di1_index >= 2 * N:
        return

    for di2_index in range(N * 2):
        # i, j
        # i+j = dia1
        # i-j+N = dia2
        # 2i + N = 1 + 2
        # i = 1 + 2 -N
        # 2j = 1 - 2 +N

        if di1_index % 2 != color:
            continue

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

        if dia2[di2_index] or dia1[di1_index]:
            continue

        dia1[di1_index] = dia2[di2_index] = True
        dfs(di1_index + 2, color, count + 1)
        dia1[di1_index] = dia2[di2_index] = False
    dfs(di1_index + 2, color, count)


dia1 = [False for _ in range(2 * N)]
dia2 = [False for _ in range(2 * N)]

dfs(0, 0, 0)
t = max_count
max_count = 0
dfs(1, 1, 0)

print(max_count + t)
