import sys
from bisect import bisect_left
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

    r = bisect_left(sequence_list_val, val)
    sequence_list_val[r] = val

print(len(sequence_list_val))
