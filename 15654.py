n, m = map(int, input().split())
seq = list(map(int, input().split()))
seq.sort()

def rec(l):
    if len(l) == m:
        print(*l, sep=" ")
        return
    for val in seq:
        if val not in l:
            rec(l + [val])
rec([])
