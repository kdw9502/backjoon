import sys

input = sys.stdin.readline

input()
seq = list(map(int, input().split()))

sequence_list_val = [seq[0]]
for val in seq:

    if sequence_list_val[-1] < val:
        sequence_list_val.append(val)
        continue
    if sequence_list_val[0] > val:
        sequence_list_val[0] = val
        continue

    l = 0
    r = len(sequence_list_val)
    while l < r:
        m = (l+r) // 2
        if sequence_list_val[m] < val:
            l = m + 1
        else:
            r = m
    sequence_list_val[r] = val

print(len(sequence_list_val))
