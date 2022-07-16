n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))


def get_safe_area(arr):
    increased = 1
    while increased:
        increased = 0
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 2:
                    if i > 0 and arr[i - 1][j] == 0:
                        arr[i - 1][j] = 2
                        increased += 1
                    if j > 0 and arr[i][j - 1] == 0:
                        arr[i][j - 1] = 2
                        increased += 1
                    if i < n - 1 and arr[i + 1][j] == 0:
                        arr[i + 1][j] = 2
                        increased += 1
                    if j < m - 1 and arr[i][j + 1] == 0:
                        arr[i][j + 1] = 2
                        increased += 1
    count = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                count += 1
    return count


max = 0


def mark(arr, depth, x, y):
    for i in range(x, n):
        for j in range(m):
            if i == x and j <= y:
                continue
            cur = copy(arr)
            if cur[i][j] != 0:
                continue
            cur[i][j] = 1
            if depth == 2:
                val = get_safe_area(copy(cur))
                global max
                if max < val:
                    max = val
                continue
            mark(cur, depth + 1, i, j)


def copy(a):
    return [x[:] for x in a]


mark(arr, 0, 0, -1)
print(max)
