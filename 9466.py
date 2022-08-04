import sys
input = sys.stdin.readline
t = int(input())

success = 1
fail = 2

for _ in range(t):
    n = int(input())
    seq = list(map(lambda x:int(x) - 1, input().split()))
    sel = [0] * n
    count = 0
    history = [0 for _ in range(n)]

    for i in range(n):
        if sel[i] != 0:
            continue
        history[i] = 1
        route = [i]
        current = seq[i]
        for _ in range(n):
            if sel[current] != 0:
                for index in route:
                    sel[index] = fail
                    count += 1
                break

            if history[current] == 1:
                val = fail
                for index in route:
                    if current == index:
                        val = success
                    sel[index] = val
                    if val == fail:
                        count += 1

                break
            history[current] = 1
            route.append(current)
            current = seq[current]

    print(count)
