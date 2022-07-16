n, m = map(int, input().split())
seq = list(map(int, input().split()))
seq.sort()


history = dict()
def rec(l, use):
    if len(l) == m:
        ans = " ".join(map(str,l))
        if ans not in history:
            print(ans)
            history[ans] = 1

        return
    for i, val in enumerate(seq):
        if use[i]  == 0:
            use[i] = 1
            rec(l + [val], use)
            use[i] = 0

rec([], [0 for i in range(n)])
