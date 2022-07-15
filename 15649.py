n, m = map(int, input().split())
seq = [i+1 for i in range(n)]

def rec(l):
    if len(l) == m:
        print(*l, sep=" ")
        return
    for i, val in enumerate(seq):
        if val not in l:
            rec(l + [val])


rec([])
