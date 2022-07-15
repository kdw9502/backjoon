n, m = map(int, input().split())
seq = [i+1 for i in range(n)]
seq.sort()

def rec(l):
    if len(l) == m:
        print(*l, sep=" ")
        return
    for i, val in enumerate(seq):
        if not l or l[-1] <= val:
            rec(l + [val])


rec([])
